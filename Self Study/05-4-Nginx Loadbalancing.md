# Nginx Loadbalancing:

### Loadbalancing Methods:
* Default Load Balance (Round robin)
* Weighted
* Session Persistence (IP Hash) => Stateful connection
* Least Connected
* Health Check

### Simple Loadbalancing:
```sh
user nginx;
worker processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

event {
    worker_connections 2048;
}
http {
    upstream lb {
        server site1.com weight=1;
        server site2.com weight=1;
    }
    server {
        listen      80 ;
        location / {
                error_log /var/log/nginx/error_root.log;
                access_log /var/log/nginx/access_root.log;
                proxy_pass http://lb;
        }
    }
}
```

### Weighted Method Load Balance:
```sh
user nginx;
worker processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

event {
    worker_connections 2048;
}
http {
    upstream lb {
        server site1.com:81 weight=1;
        server site2.com:82 weight=2;
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
}
```

### Least Connection Method Load Balance:
```sh
user nginx;
worker processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

event {
    worker_connections 2048;
}
http {
    upstream lb {
        least_conn;
        server site1.com:81 ;
        server site2.com:82 ;
        server site2.com:83 ;
    }
}
```

### IP Hash Method Load Balance:
```sh
user nginx;
worker processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

event {
    worker_connections 2048;
}
http {
    upstream lb {
        ip_hash;
        server site1.com:81 ;
        server site2.com:82 ;
        server site2.com:83 ;
    }
}
```

### Health Check Method Load Balance:
```sh
user nginx;
worker processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

event {
    worker_connections 2048;
}
http {
    upstream lb {
        server site1.com:81 weight=5;
        server site2.com:82 max_fails=3 fail_timeout=30s;
        server site2.com:83;
    }
}
```





