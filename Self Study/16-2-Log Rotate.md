# Log Rotate

### Logrotate Responsibility:
* Splitting large log files
* Keep multiple old versions (rotation)
* Compressing old logs
* Deleting very old logs

### Logrotate Configuration file:
* `/etc/logrotate.conf` : General settings (Number of versions, compression, ...)
* `/etc/logrotate.d/` : Services directory (nginx, apache2, mysql, ...)

### Logrotate Simple Configuration:
```sh
/var/log/syslog {
    daily             # Rotate every day
    rotate 7          # Keep 7 logs (One week)
    size 10M          # Rotate when size of log reach 10MB
    compress          # Compress old logs with Gzip
    missingok         # Get no error, if no log
    notifempty        # Do not rotate if no log
    create 0640 syslog adm   # New logs with this permission
    postrotate
        /usr/lib/rsyslog/rsyslog-rotate  # Reload service after rotation
    endscript
}
```

### Logrotate files naming:
```sh
/var/log/syslog        # Current log
/var/log/syslog.1      # Yesterday log
/var/log/syslog.2.gz   # Logs of two days ago
/var/log/syslog.3.gz   # Logs of three days ago
```

### Manual Logrotate:
```sh
logrotate -f /etc/logrotate.conf
```

### Sample Nginx Logrotate:

```sh
/var/log/nginx/*.log {
    daily                # Rotate every day
    rotate 14            # Keep 14 logs/days
    size 10M             # Rotate when size of log reach 10MB
    compress             # Compress old logs with Gzip
    delaycompress        # Do not compress yesterday log
    missingok            # Get no error, if no log
    notifempty           # Do not rotate if no log
    create 0640 www-data adm   # New logs with this permission
    sharedscripts        # Postrotate script will run once (Not for each file)

    postrotate
        if [ -f /var/run/nginx.pid ]; then
            kill -USR1 `cat /var/run/nginx.pid` 
        fi
    endscript
}
# After each rotation send USR1 signal to Nginx to create new log
```

### Filtering Severity:
* To keep just important logs with priority
```sh
# On client:
if ($programname == "nginx" and $syslogseverity <= 4) then /var/log/remote/nginx_important.log
```




