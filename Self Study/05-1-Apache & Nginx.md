# Apache & Nginx

### Apache:

```bash
apt install apache2
systemctl status apache2
systemctl enable --now apache2
curl http://localhost # Test Service
```

#### Apache Important Paths:
* `/var/www/html/` : Default Web Page
* `/etc/apache2/apache2.conf` : Main Config file
* `/etc/apache2/sites-available/` : Virtual Hosts
* `/etc/apache2/sites-enabled/` : Symbolic Links

### Apache Virtual Hosts:

#### Create two sites with different domain name:
* `test1.local`
* `test2.local`

```bash
# Create directory for each site:
mkdir -p /var/www/test1.local/public_html
mkdir -p /var/www/test2.local/public_html

# Set permissions:
chown -R $USER:$USER /var/www/test1.local
chown -R $USER:$USER /var/www/test2.local

# Create a simple index file for each site:
echo "<h1>Site 1 - test1.local</h1>" > /var/www/test1.local/public_html/index.html
echo "<h1>Site 2 - test2.local</h1>" > /var/www/test2.local/public_html/index.html
```

**Create Virtual Host File for each site**
```bash
# test1.local:
nano /etc/apache2/sites-available/test1.local.conf # Create & edit config file

# Configuration:
<VirtualHost *:80>
    ServerAdmin webmaster@test1.local
    ServerName test1.local
    DocumentRoot /var/www/test1.local/public_html
    ErrorLog ${APACHE_LOG_DIR}/test1_error.log
    CustomLog ${APACHE_LOG_DIR}/test1_access.log combined
</VirtualHost>

# test2.local:
nano /etc/apache2/sites-available/test2.local.conf # Create & edit config file

# Configuration:
<VirtualHost *:80>
    ServerAdmin webmaster@test2.local
    ServerName test2.local
    DocumentRoot /var/www/test2.local/public_html
    ErrorLog ${APACHE_LOG_DIR}/test2_error.log
    CustomLog ${APACHE_LOG_DIR}/test2_access.log combined
</VirtualHost>
```

**a2ensite:**
> `a2ensite` is used to enable virtual hosts. When running it will create a symbolic link of site configuration file in `/etc/apache2/sites-enabled/` path.
```bash
a2ensite Site-Config-Name # Enable Virtual Host
systemctl reload apache2 # Needed after enabling virtual host
```

#### Enable Virtual Hosts:
```bash
a2ensite test1.local.conf
a2ensite test2.local.conf
systemctl reload apache2
```
**a2dissite:**
> `a2disiste` is used to disable virtual host and remove the config file from `/sites-enabled/` path.
```
bash
a2dissite site.example.com
```

### Apache Log Files:

* `/var/log/apache2/access.log` : Access Logs
* `/var/log/apache2/error.log` : Error Logs

**Logs content:**
* `Access Logs` : All requests data (URL, IP, Browser, Time, HTTP Status code, Request Type, Size, ...)
* `Error Logs` : Apache errors, File errors, Permissions, Closed ports, CGI & PHP errors, ...

**Access Log Format:**
```bash
192.168.1.10 - - [19/Jul/2025:14:33:12 +0330] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0"
```

**Real-time Logs:**
```bash
tail -f /var/log/apache2/test1_access.log
```

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

```bash
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

# Restart Nginx
systemctl restart nginx
```

#### Nginx Errors:

* `403 Forbidden` : File or Directory permission error
* `404 Not Found` : index.html not exist or wrong path
* `502 Bad Gateway` : Backend not responding
* `port already in use` : Socket/port is busy by another service
* `unexpected end of file` : In configuration file, `}` is missing or used more than usual.

#### Nginx Troubleshoot:
```bash
systemctl status nginx # Check the service
journalctl -xeu nginx # See details of problem if there is a problem
```

**Nginx Logs:**
* `/var/log/nginx/access.log` : Access Logs
* `/var/log/nginx/error.log` : Error Logs

```bash
tail -f /var/log/nginx/error.log
tail -f /var/log/nginx/access.log
```
```bash
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
```bash
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
```bash
ln -s /etc/nginx/sites-available/test3.local /etc/nginx/sites-enabled/
nginx -t
systemctl reload nginx
```

#### Nginx ReverseProxy Configuration with SSL:

```bash
server {
    listen 443 ssl;
    server_name test3.local;

    ssl_certificate     /etc/ssl/certs/test3.local.crt;
    ssl_certificate_key /etc/ssl/private/test3.local.key;
    ssl_trusted_certificate /etc/ssl/certs/test3.local.ca-bundle.crt;

    location / {
        proxy_pass http://127.0.0.1:8080;
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
```bash
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

### Apache vs Nginx:

| ویژگی                                                  | **Apache**                                         | **Nginx**                                           |
| ------------------------------------------------------ | -------------------------------------------------- | --------------------------------------------------- |
| 🔁 مدل پردازش                                          | *process/thread based* (Prefork/Worker/Event)      | *event-driven*، async، non-blocking                 |
| 🚀 سرعت پاسخ‌دهی به درخواست‌های ایستا (static content) | کندتر نسبت به Nginx                                | بسیار سریع‌تر، مخصوصاً در بار بالا                  |
| 🔌 مصرف RAM و CPU                                      | بالاتر (در ترافیک زیاد)                            | بسیار کمتر و بهینه‌تر                               |
| 🔧 پیکربندی                                            | ساده‌تر برای شروع و انعطاف‌پذیرتر برای `.htaccess` | کانفیگ تمیزتر ولی مفاهیم کمی سخت‌تر                 |
| 🔐 پشتیبانی از `.htaccess`                             | ✅ دارد (برای هر فولدر مجزا)                        | ❌ ندارد (تمام تنظیمات در فایل مرکزی)                |
| 🔁 پشتیبانی از reverse proxy                           | به‌صورت ماژول اضافه (mod\_proxy)                   | داخلی و بسیار قدرتمند                               |
| 📊 Performance در ترافیک بالا                          | افت می‌کنه به‌دلیل معماری process-based            | مقیاس‌پذیری عالی با منابع کمتر                      |
| 🧩 ماژول‌پذیری                                         | داینامیک و runtime (بارگزاری هنگام اجرا)           | ماژول‌ها باید موقع کامپایل مشخص بشن                 |
| 🔍 لاگ‌گیری                                            | ساده، قابل سفارشی‌سازی                             | پیش‌فرض ساده، ولی نیاز به تنظیمات بیشتر برای جزئیات |
| 📦 نصب پیش‌فرض در بیشتر سیستم‌ها                       | بله (مثلاً در Debian, Ubuntu)                      | معمولاً نه، باید نصب شه                             |
| 👥 جامعه کاربری و مستندات                              | بسیار گسترده و قدیمی                               | گسترده، رو به رشد سریع                              |




