# Apache

### Install Apache:

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
# Test configuration before run:
apache2ctl configtest
systemctl reload apache2
```
**a2dissite:**
> `a2disiste` is used to disable virtual host and remove the config file from `/sites-enabled/` path.
```bash
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




