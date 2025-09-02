# Nginx Limitations


```sh
user nginx;
worker processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

event {
    worker_connections 2048;
}

http {
        limit_conn_zone $server_name zone=new_zone:5m; # Connection Zone: Using some space of memory for connections
        limit_req_zone $binary_remote_addr zone=onerps:10m rate:1r/s; # Request Zone: Using some space of memory for requests (request per second)
        server {
                listen 80;
                root /var/www/html/;
                location / {
                }
                location /auth { # Order is important:
                        error_log /var/log/nginx/error_auth.log;
                        access_log /var/log/nginx/access_auth.log;
                        satisfy all;
                        allow 172.16.2.1;   # Allow this IP Address
                        deny all;           # Deny all others
                        auth_basic          "test for login";
                        auth_basic_user_file /etc/nginx/.htpasswd; # Authenticate using htpasswd file
                }
                location /test_zone {
                        limit_rate 50k; # Bandwidth limitation 
                        limit_conn new_zone 1;
                        limit_req zone=onerps burst=5 ; # Limit requests per second
                }
        }
}
```







