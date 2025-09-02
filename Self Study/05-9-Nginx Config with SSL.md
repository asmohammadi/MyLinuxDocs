# Nginx Configuration with SSL:


### Nginx Configuration with SSL (Let's Encrypt):

```bash
# Address: https://test3.local:8443
server {
    listen 8443 ssl;
    server_name test3.local;

    root /var/www/test3.local;
    index index.html;

    ssl_certificate     /etc/ssl/certs/test3.local.crt;
    ssl_certificate_key /etc/ssl/private/test3.local.key;

    access_log /var/log/nginx/test3_access.log;
    error_log  /var/log/nginx/test3_error.log;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Nginx Configuration with Real SSL:
```bash
server {
    listen 8443 ssl;
    server_name test3.local;

    root /var/www/test3.local;
    index index.html;

    ssl_certificate     /etc/ssl/certs/test3.local.crt;
    ssl_certificate_key /etc/ssl/private/test3.local.key;
    ssl_trusted_certificate /etc/ssl/certs/test3.local.ca-bundle.crt;

    access_log /var/log/nginx/test3_access.log;
    error_log  /var/log/nginx/test3_error.log;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Nginx Configuration with PEM:
```bash
server {
    listen 8443 ssl;
    server_name test3.local;

    root /var/www/test3.local;
    index index.html;

    ssl_certificate     /etc/ssl/certs/test3.local.pem; # Main Cert (domain.pem / cert.pem)
    ssl_certificate_key /etc/ssl/private/test3.local.key; # Private Key
    ssl_trusted_certificate /etc/ssl/certs/test3.local.chain.pem; # CA (chain.pem / ca_bundle.pem)

    access_log /var/log/nginx/test3_access.log;
    error_log  /var/log/nginx/test3_error.log;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Configuration with Real SSL & Redirect:
* Redirect port 80 to 8443
* Redirect port 443 to 8443

```bash
# Redirect Http(80) to https://test3.local:8443
server {
    listen 80;
    server_name test3.local;

    return 301 https://$host:8443$request_uri;
}

# Redirect Https(443) to https://test3.local:8443
server {
    listen 443 ssl;
    server_name test3.local;

    ssl_certificate     /etc/ssl/certs/test3.local.crt;
    ssl_certificate_key /etc/ssl/private/test3.local.key;
    ssl_trusted_certificate /etc/ssl/certs/test3.local.ca-bundle.crt;

    return 301 https://$host:8443$request_uri;
}

# VirtualHost with 8443:
server {
    listen 8443 ssl;
    server_name test3.local;

    root /var/www/test3.local;
    index index.html;

    ssl_certificate     /etc/ssl/certs/test3.local.crt;
    ssl_certificate_key /etc/ssl/private/test3.local.key;
    ssl_trusted_certificate /etc/ssl/certs/test3.local.ca-bundle.crt;

    access_log /var/log/nginx/test3_access.log;
    error_log  /var/log/nginx/test3_error.log;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Redirect 80 to 443 & Redirect path with Real SSL:

```bash
server {
    listen 80;
    server_name site1.example.com;

    # Redirect Http to Https:
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name site1.example.com;

        ssl_certificate     /etc/ssl/certs/site1.example.com.crt;
    ssl_certificate_key /etc/ssl/private/site1.example.com.key;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    # Redirect home path / to /ecco:
    location = / {
        return 301 https://$host/ecco;
    }

    location / {
        proxy_pass http://127.0.0.1:8080;  # Apache is on port 8080
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```





