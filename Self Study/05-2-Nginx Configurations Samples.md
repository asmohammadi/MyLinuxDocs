# Nginx Configurations Samples

### Nginx Simple Configuration:
```sh
user nginx;
worker processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

event {
    worker_connections 2048;
}
http {
    server {
        listen      8080;
        location / {
                error_log /var/log/nginx/error_root.log;
                access_log /var/log/nginx/access_root.log;
                root    /var/www/nginx ;
        }
        location /images {
                error_log /var/log/nginx/error_images.log;
                access_log /var/log/nginx/access_images.log;
                root    /var/www/nginx ;
        }
    }
}
```

### Nginx Configuration Sample:

```sh
user nginx;
worker processes auto;
error_log /var/log/nginx/error.log;
access_log /var/log/nginx/access.log;
pid /run/nginx.pid;

event {
    worker_connections 2048;
}
http {
    server {
        listen      80;
        location / {
                error_log /var/log/nginx/error_root.log;
                access_log /var/log/nginx/access_root.log;
                root    /var/www/nginx ;
        }
        # Limit directory to these formats
        location ~ \.(mp3|mp4) { # Files like ".mp3" or ".mp4"
                error_log /var/log/nginx/error_audio.log;
                access_log /var/log/nginx/access_audio.log;
                root    /var/www/media/audio ;
                sendfile            on;
                sendfile_max_chunk  1m;
        }
        # Limit directory to these formats
        location ~ \.(jpeg|png|jpg) { # Files like ".jpeg" or ".png" or ".jpg"
                error_log /var/log/nginx/error_pictures.log;
                access_log /var/log/nginx/access_pictures.log;
                root    /var/www/media/pictures ;
                sendfile            on;
                sendfile_max_chunk  1m;
        }
        # HTTP Response Codes:
        location /404 {
                return 404;
        }
        location /301 {
                return 301 http://linux.ir;
        }
        location /302 {
                return 302 http://linux.ir;
        }
    }
}
```

**HTTP Response Codes:**
* `1XX` : Information response
* `2XX` : Successful response
* `3XX` : Redirect response
* `4XX` : Client error response
* `5XX` : Server error response






