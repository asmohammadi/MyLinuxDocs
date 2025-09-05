# Apache Configurations with SSL:

### Configuration with Real SSL:

```bash
# Address: https://test3.local:8443
<VirtualHost *:8443>
    ServerName test3.local

    DocumentRoot /var/www/test3.local
    DirectoryIndex index.html

    SSLEngine on
    SSLCertificateFile      /etc/ssl/certs/test3.local.crt
    SSLCertificateKeyFile   /etc/ssl/private/test3.local.key
    SSLCertificateChainFile /etc/ssl/certs/test3.local.ca-bundle.crt

    ErrorLog  ${APACHE_LOG_DIR}/test3_error.log
    CustomLog ${APACHE_LOG_DIR}/test3_access.log combined

    <Directory /var/www/test3.local>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```
```bash
# Create directory & index file:
mkdir -p /var/www/test3.local
echo "<h1>Apache on Port 8443 with Paid SSL</h1>" | tee /var/www/test3.local/index.html
```
```bash
# Enable SSL Module:
a2enmod ssl
```
```bash
# Add port 8443 to Apache configuration:
nano /etc/apache2/ports.conf # Edit port configuration
# Add this line:
Listen 8443
# or with one command:
sed -i 's/Listen 80/Listen 8443/' /etc/apache2/ports.conf # Change 80 to 8443
```
```bash
# Enable site:
a2ensite test3.local.conf
```
```bash
# Test & reload Apache:
apache2ctl configtest
systemctl reload apache2
```

### Configuration with Real SSL & Redirect:

* Redirect port 80 to 8443
* Redirect port 443 to 8443

```bash
# Redirect Http(80) to https://test3.local:8443
<VirtualHost *:80>
    ServerName test3.local

    # Redirect all requests to 8443
    Redirect permanent / https://test3.local:8443/
</VirtualHost>

# Redirect Https(443) to https://test3.local:8443
<VirtualHost *:443>
    ServerName test3.local

    SSLEngine on
    SSLCertificateFile      /etc/ssl/certs/test3.local.crt
    SSLCertificateKeyFile   /etc/ssl/private/test3.local.key
    SSLCertificateChainFile /etc/ssl/certs/test3.local.ca-bundle.crt

    # Redirect all requests to 8443
    Redirect permanent / https://test3.local:8443/
</VirtualHost>

# VirtualHost with 8443
<VirtualHost *:8443>
    ServerName test3.local

    DocumentRoot /var/www/test3.local
    DirectoryIndex index.html

    SSLEngine on
    SSLCertificateFile      /etc/ssl/certs/test3.local.crt
    SSLCertificateKeyFile   /etc/ssl/private/test3.local.key
    SSLCertificateChainFile /etc/ssl/certs/test3.local.ca-bundle.crt

    <Directory /var/www/test3.local>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog  ${APACHE_LOG_DIR}/test3_error.log
    CustomLog ${APACHE_LOG_DIR}/test3_access.log combined
</VirtualHost>
```
```bash
# Test & Enable ssl module:
a2enmod ssl
apache2ctl configtest
systemctl reload apache2
```






