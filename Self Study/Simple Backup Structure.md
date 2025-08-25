# Simple Backup Structure:


##  Archive Directory Structure:

```lua
Linux-admin-week01-backup/
├── config/
│   ├── sshd_config
│   ├── ufw.rules
│   ├── apache-vhost.conf
│   └── nginx-vhost.conf
├── ssl/
│   ├── certbot-certificates.txt
│   └── example.com-fullchain.pem
├── scripts/
│   ├── backup-script.sh
│   └── reload-nginx.sh
├── logs/
│   ├── journalctl.log
│   └── fail2ban-status.txt
├── screenshots/
│   └── *.png
└── README.md
```

```sh
# Backup SSH:
cp /etc/ssh/sshd_config ~/linux-admin-week1-backup/config/

# Backup Web Server configurations:
cp /etc/nginx/sites-available/test ~/linux-admin-week1-backup/config/nginx-vhost.conf
cp /etc/apache2/sites-available/test.conf ~/linux-admin-week1-backup/config/apache-vhost.conf

# Backup Certificates:
certbot certificates > ~/linux-admin-week1-backup/ssl/certbot-certificates.txt

# Backup Logs:
journalctl -xe > ~/linux-admin-week1-backup/logs/journalctl.log
fail2ban-client status sshd > ~/linux-admin-week1-backup/logs/fail2ban-status.txt

# Archive all Configurations Backups:
tar -czvf linux-admin-week1-backup.tar.gz linux-admin-week1-backup/
```


