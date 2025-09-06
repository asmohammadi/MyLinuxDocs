# Installing SSL (Let's Encrypt):

### Certbot:
```bash
# Install for Nginx:
apt install certbot python3-certbot-nginx

# Install for Apache:
apt install certbot python3-certbot-apache

# Check installation:
certbot --version
```

### Check DNS Records:
```bash
dig +short example.com
nslookup example.com
```

### Issue SSL for Nginx:
```bash
certbot --nginx -d example.com -d www.example.com
# Give Email address for renew SSL
# Agree term of service
# Enable Redirect Http to Https
```

### Issue SSL for Apache:
```bash
certbot --apache -d example.com -d www.example.com
# Give Email address for renew SSL
# Agree term of service
# Enable Redirect Http to Https
```
* Now Apache Virtual Host will be edited
* New block for 443 will be created.
* The path of .pem certificates will added to file.
* Https address wil be activated.

### Check & Test installed Certificates:
```bash
certbot certificates
# Display the path of Certificates
# Display the expiration date of Certs
# Display certificates Domain Names
```
```bash
# Manual test:
curl -I https://example.com
# True answer:
HTTP/1.1 200 OK
Redirect 301/302
```
```bash
# Testing Certificates:
openssl x509 -in /etc/letsencrypt/live/example.com/fullchain.pem -text -noout
```

### Auto-Renew SSL:

1. systemd timer:
```bash
systemctl list-timers | grep certbot
# Answer:
certbot.timer     ...  Mon 2025-07-22 ...  systemd-timers
```

2. Dry-run:
```bash
certbot renew --dry-run

# Answer:
all renewals succeeded
```

3. Cron:
```bash
crontab -e
# Add this line:
0 3 * * * certbot renew --quiet # Every day at 03:00 AM
```

#### Create hook to reload Nginx after Renew:
```bash
# Create .sh file:
nano /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh
# Add this:
#!/bin/bash
systemctl reload nginx
# Make it executable:
chmod +x /etc/letsencrypt/renewal-hooks/deploy/reload-nginx.sh
```

### Let's Encrypt Limitations:

* `Expiration` : 90 days
* `Renew` : Every 60 days & Need Internet
* `Issue Limit` : 5 SSL per week for each Domain
* `Subdomains` : Up to 100
* `Wildcard` : No Wildcard
* `Security` : Certificates must be in path `/etc/letsencrypt/live/`. Only Root have permission.


 






