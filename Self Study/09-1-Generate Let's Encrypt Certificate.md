# Generate Let's Encrypt Certificate

## Steps to install Let's Encrypt SSL on Ubuntu 24.04:
1. Update your system:
```bash
sudo apt update && sudo apt upgrade 
```
2. Install `Certbot` and the `Apache` or `Nginx` plugin:
```bash
# For Apache:
apt install certbot python3-certbot-apache. 
# For Nginx:
apt install certbot python3-certbot-nginx. 
```
3. Configure your web server (example with Apache):
```bash
# Edit your virtual host file:
(e.g., /etc/apache2/sites-available/example.com.conf). 
# Ensure the ServerName and ServerAlias directives are correctly set. 
# Enable the site and required modules:
a2ensite example.com and sudo a2enmod ssl. 
# Test and reload Apache:
apache2ctl configtest
systemctl reload apache2. 
```
4. Obtain and install the SSL certificate:
```bash
# For Apache:
certbot --apache -d example.com -d www.example.com
# For Nginx:
certbot --nginx -d example.com -d www.example.com
```
> Certbot will guide you through the process, including prompting for your email and agreeing to the terms of service. 
> Note that you will need to allow HTTP traffic (port 80) for the initial verification by Let's Encrypt. 

5. Set up `automatic renewal`:

> Certbot automatically configures a cron job or systemd timer to renew your certificates before they expire (usually every 90 days). 

You can test the renewal process with
```bash
certbot renew --dry-run. 
```

### Important Considerations:

#### Internet connection:

> While the certificate can be used offline after it's generated, you will need an internet connection for the initial issuance and for automatic renewals. 

#### Firewall:

> Ensure port 80 (for initial verification) and 443 (for HTTPS) are open in your firewall.
```bash
sudo ufw allow 80
sudo ufw allow 443
```

#### Domain validation:

> Make sure your domain name is correctly pointing to your server's IP address. 

#### Virtual host configuration:

> Double-check your virtual host file to ensure it's correctly configured for your domain. 


