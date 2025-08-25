# Centralized Logging (rsyslog)

### rsyslog:
* `rsyslog` is using for sending all servers logs to a Log Server.
* Its a daemon for collecting and sending logs.
* Using UDP/TCP protocols.
* It can send logs to File, Database or even Cloud Services.

### Configuring a Log Server:
> Need to edit `/etc/rsyslog.conf` or `/etc/rsyslog.d/50-default.conf`
```sh
# Log Server Address: 192.168.1.100 
# UDP syslog reception
module(load="imudp")
input(type="imudp" port="514")

# TCP syslog reception
module(load="imtcp")
input(type="imtcp" port="514")

# Saving all logs in a specific path:
*.*   /var/log/remote.log
```
```sh
# Restart rsyslog:
systemctl restart rsyslog
```

### Configuring Clients (Servers):
> Need to edit `/etc/rsyslog.conf` or `/etc/rsyslog.d/50-default.conf`
```sh
# Log Server Address: 192.168.1.100 
*.*   @@192.168.1.100:514 # Using TCP connection
*.*   @192.168.1.100:514 # Using UDP connection
systemctl restart rsyslog
```

### Sample for Log Server:
* 3 Servers
* Each server has 3 services
* Each service must have its own logs in a specific path

```sh
# Log server structure:
/var/log/remote/
    ├── web1/
    │   ├── nginx.log
    │   ├── apache2.log
    │   └── sshd.log
    ├── web2/
    │   ├── nginx.log
    │   ├── apache2.log
    │   └── sshd.log
    └── db1/
        ├── mysqld.log
        └── sshd.log
```
```sh
# Log server config file:
    # /etc/rsyslog.d/central.conf
    # /etc/rsyslog.conf

# Load TCP/UDP modules
module(load="imudp")
input(type="imudp" port="514")
module(load="imtcp")
input(type="imtcp" port="514")

# Template for host + service based logs
$template RemoteLogs,"/var/log/remote/%HOSTNAME%/%PROGRAMNAME%.log"

# Store all logs using the template
*.* ?RemoteLogs
```

### Log files Samples:

```sh
# /var/log/remote/web1/sshd.log
Aug 16 20:12:34 web1 sshd[2034]: Accepted password for asghar from 192.168.1.50 port 51234 ssh2
Aug 16 20:13:01 web1 sshd[2034]: pam_unix(sshd:session): session opened for user asghar by (uid=0)
Aug 16 20:45:22 web1 sshd[2501]: Failed password for root from 10.0.0.5 port 40322 ssh2

# /var/log/remote/web2/nginx.log
Aug 16 21:05:12 web2 nginx[1205]: 192.168.1.51 - - [16/Aug/2025:21:05:12 +0330] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0"
Aug 16 21:05:13 web2 nginx[1205]: 192.168.1.51 - - [16/Aug/2025:21:05:13 +0330] "POST /login HTTP/1.1" 302 512 "-" "Mozilla/5.0"

# /var/log/remote/db1/mysqld.log
2025-08-16T18:22:31.345678Z 0 [Note] mysqld (mysqld 8.0.30) starting as process 2154
2025-08-16T18:22:33.567890Z 2 [Warning] Access denied for user 'root'@'192.168.1.55' (using password: YES)
2025-08-16T18:23:01.234567Z 3 [Note] Connection id 5 accepted from 192.168.1.50
```

### Logrotate on Log Server:

```sh
# /etc/logrotate.d/remote-logs
/var/log/remote/*/*.log {
    daily
    missingok
    rotate 30
    size 10M
    compress
    delaycompress
    notifempty
    create 0640 syslog adm
    sharedscripts

    postrotate
        systemctl reload rsyslog >/dev/null 2>&1 || true # Reload rsyslog
    endscript
}
```

### Logrotate for Multi Service & Time:
```sh
# SSH logs (7 days)
/var/log/remote/*/sshd.log {
    daily
    rotate 7
    size 10M
    compress
    delaycompress
    missingok
    notifempty
    create 0640 syslog adm
    postrotate
        systemctl reload rsyslog >/dev/null 2>&1 || true
    endscript
}

# Nginx logs (14 days)
/var/log/remote/*/nginx.log {
    daily
    rotate 14
    size 10M
    compress
    delaycompress
    missingok
    notifempty
    create 0640 syslog adm
    postrotate
        systemctl reload rsyslog >/dev/null 2>&1 || true
    endscript
}

# MySQL logs (30 days)
/var/log/remote/*/mysqld.log {
    daily
    rotate 30
    size 10M
    compress
    delaycompress
    missingok
    notifempty
    create 0640 syslog adm
    postrotate
        systemctl reload rsyslog >/dev/null 2>&1 || true
    endscript
}
```
```sh
# Result:
sshd.log       sshd.log.1      sshd.log.2.gz     ...   sshd.log.7.gz
nginx.log      nginx.log.1     nginx.log.2.gz    ...   nginx.log.14.gz
mysqld.log     mysqld.log.1    mysqld.log.2.gz   ...   mysqld.log.30.gz
```









