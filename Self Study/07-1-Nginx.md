# Nginx

### Nginx & Virtual Host:

#### Nginx Important Paths:
* `/var/www/html/` : Default Web Page
* `/etc/nginx/nginx.conf` : Main Config file
* `/etc/nginx/sites-available/` : Virtual Hosts
* `/etc/nginx/sites-enabled/` : Symbolic Links
* `/var/log/nginx/error.log` : Error Logs

**Scenario:**
* `Apache` : test1.local
* `Nginx` : test2.local:8080

#### Create Virtual Host:

```sh
# Create configuration file:
nano /etc/nginx/sites-available/test2.local

# Edit configuration:
server {
    listen 8080;
    server_name test2.local;

    root /var/www/test2.local;
    index index.html;

    access_log /var/log/nginx/test2_access.log;
    error_log /var/log/nginx/test2_error.log;

    location / {
        try_files $uri $uri/ =404;
    }
}

# Enable Virtual Host for Nginx:
ln -s /etc/nginx/sites-available/test2.local /etc/nginx/sites-enabled/

# Test Nginx configuration:
nginx -t

# Reload Nginx
systemctl reload nginx
```

#### Nginx Errors:

* `403 Forbidden` : File or Directory permission error
* `404 Not Found` : index.html not exist or wrong path
* `502 Bad Gateway` : Backend not responding
* `port already in use` : Socket/port is busy by another service
* `unexpected end of file` : In configuration file, `}` is missing or used more than usual.

#### Nginx Troubleshoot:
```sh
nginx -c /etc/nginx/nginx.conf -t # Test Nginx configuration
systemctl status nginx # Check the service
systemctl reload nginx # Read configuration again and run it (Without changing PID of workers)
systemctl restart nginx # Will kill the worker process & start it again
journalctl -xeu nginx # See details of problem if there is a problem (Recently logs)
```

**Nginx Logs:**
* `/var/log/nginx/access.log` : Access Logs
* `/var/log/nginx/error.log` : Error Logs

```sh
tail -f /var/log/nginx/error.log
tail -f /var/log/nginx/access.log
```
```sh
192.168.1.15 - - [19/Jul/2025:17:24:01 +0330] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0"
```

### Nginx as a ReverseProxy for APAche:
```sh
# Scenario:
Client ──► Nginx (80/443) ──► Apache (8080/8443)
```

1. **Apache on Port 8080:**
```bash
<VirtualHost *:8080>
    ServerName test3.local
    DocumentRoot /var/www/test3.local
    ...
</VirtualHost>
```

2. **Nginx ReverseProxy Configuration:**
```sh
server {
    listen 80;
    server_name test3.local;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
* `$host` : Request address
* `$remote_addr` : Client IP Address
* `$proxy_add_x_forwarded_for` : Proxy IP Address + Client IP Address


3. **Enable Sites in Nginx:**
```sh
ln -s /etc/nginx/sites-available/test3.local /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx
```

#### Nginx ReverseProxy Configuration with SSL:

```sh
server {
    listen 443 ssl;
    server_name test3.local;

    ssl_certificate     /etc/ssl/certs/test3.local.crt;
    ssl_certificate_key /etc/ssl/private/test3.local.key;
    ssl_trusted_certificate /etc/ssl/certs/test3.local.ca-bundle.crt;

    location / {
        proxy_pass https://127.0.0.1:8443;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

# Redirect port 80 → 443 (Optional)
server {
    listen 80;
    server_name test3.local;

    return 301 https://$host$request_uri;
}
```
```sh
# Apache Configuration:
<VirtualHost 127.0.0.1:8080>
    ServerName test3.local
    DocumentRoot /var/www/test3.local

    <Directory /var/www/test3.local>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog  ${APACHE_LOG_DIR}/test3_error.log
    CustomLog ${APACHE_LOG_DIR}/test3_access.log combined
</VirtualHost>
```




