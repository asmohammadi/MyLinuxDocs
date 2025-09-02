# Nginx Modules

```sh
# Path of Nginx Modules:
/usr/lib64/nginx/modules/
```

### Using Stream Module:
```sh
load_module /usr/lib64/nginx/modules/ngx_stream_module.so;
user nginx;
worker processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

event {
    worker_connections 2048;
}
# Load Balance using TCP:
stream {
    upstream tcp_check {
        server site1.com:81 ;
        server site2.com:82 ;
        server site2.com:83 ;
    server {
        listen 8081 ;
        proxy_pass tcp_check;
    }
}
# Load Balance using HTTP:
http {
    upstream lb {
        ip_hash;
        server site1.com:81 ;
        server site2.com:82 ;
        server site2.com:83 ;
    }
    server {
        listen      80 ;
        location / {
                error_log /var/log/nginx/error_root.log;
                access_log /var/log/nginx/access_root.log;
                proxy_pass http://lb;
        }
    }
    server {
        listen      81 ;
        location / {
                root    /var/www/nginx/server1;
        }
    }
    server {
        listen      82 ;
        location / {
                root    /var/www/nginx/server2;
        }
    }
    server {
        listen      83 ;
        location / {
                root    /var/www/nginx/server3;
        }
    }
}
```





