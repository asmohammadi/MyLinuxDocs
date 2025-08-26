# Log Management Basic Scenario

### Scenario:
* Centralized logs with rsyslog, filtering important logs, rotation, compression, different retention for each service, and archive old logs for long time on NFS.
* Log Server: 192.168.1.100
* NFS : 192.168.1.200
* Clients : web1 (192.168.1.10), web2 (192.168.1.11), db1 (192.168.1.20)
* Services : nginx, sshd, mysqld
* Filtering:
  * sshd : severity ≤ err (3)
  * mysqld : severity ≤ warning (4)
  * nginx : severity ≤ warning (4)
* Log Server Path : `/var/log/remote/<host>/<service>.log`
* Dynamic pattern for saving structure on rsyslog:
  * /var/log/remote/%HOSTNAME%/%PROGRAMNAME%.log
* NFS PATH:
  * NFS Server : `/srv/log-archive`
  * Log Server : `/mnt/log-archive`
* Sending logs method:
  * TCP : Port 514, Forward rules on clients
* Logrotate:
  * sshd : Daily, compress, size 50M, rotate 7
  * nginx : Daily, compress, size 100M, rotate 14
  * mysqld : Daily, compress, size 200M, rotate 30
* NFS Archiving:
  * Postrotate script : Move from `log.2.gz.*` and older to `/mnt/log-archive/<host>/` , Keep 2 days logs
* Security & Permissions: syslog:adm, 0750 permission

### Enable Logging for Nginx:
```sh
error_log syslog:server=unix:/dev/log;
access_log syslog:server=unix:/dev/log combined;
# or:
error_log syslog:server=127.0.0.1:514,facility=local7,tag=nginx_error;
access_log syslog:server=127.0.0.1:514,facility=local7,tag=nginx_access;
```

### Enable Logging for MysqlD:
```sh
# /etc/mysql/mysql.conf.d/mysqld.cnf
[mysqld_safe]
syslog
# or:
[mysqld]
log_syslog=ON
```

### Enable logging for Nginx & MysqlD using Agent:
* Using `Filebeat` , `rsyslog imfile` or `fluent-bit`.
```sh
# In rsyslog:
module(load="imfile")
input(type="imfile" File="/var/log/nginx/access.log" Tag="nginx_access" Severity="info" Facility="local6")
input(type="imfile" File="/var/log/nginx/error.log"  Tag="nginx_error"  Severity="error" Facility="local6")
```

### Log Server Rsyslog:
```sh
# Filtering + Receiving + Dynamic Path
# /etc/rsyslog.d/10-central-receiver.conf:

# Enable receivers
module(load="imudp")
input(type="imudp" port="514")
module(load="imtcp")
input(type="imtcp" port="514")

# Template: split by host + program (service)
template(name="RemoteLogsPath" type="string"
         string="/var/log/remote/%HOSTNAME%/%PROGRAMNAME%.log")

# Make sure rsyslog auto-creates directories for dynaFile actions
# (available in modern rsyslog)
global(workDirectory="/var/spool/rsyslog")

# Filter: only important logs for these services
# sshd: severity <= err(3)
if ($programname == "sshd" and $syslogseverity <= 3) then {
    action(type="omfile" dynaFile="RemoteLogsPath" dynaFileCreatePath="on")
    stop
}

# nginx: severity <= warning(4)
if ($programname == "nginx" and $syslogseverity <= 4) then {
    action(type="omfile" dynaFile="RemoteLogsPath" dynaFileCreatePath="on")
    stop
}

# mysqld: severity <= warning(4)
if ($programname == "mysqld" and $syslogseverity <= 4) then {
    action(type="omfile" dynaFile="RemoteLogsPath" dynaFileCreatePath="on")
    stop
}

# (Optional) drop other remote noise
# if $fromhost-ip != "127.0.0.1" then stop
```
```sh
# Enable:
mkdir -p /var/log/remote
chown -R syslog:adm /var/log/remote
chmod -R 0750 /var/log/remote
systemctl restart rsyslog
```

### Clients Rsyslog:

```sh
# Forwarders + Filtering:
# /etc/rsyslog.d/90-forward-important.conf

# Forward important logs to central server via TCP
# sshd: <= err(3)
if ($programname == "sshd" and $syslogseverity <= 3) then {
    action(type="omfwd" target="192.168.1.100" port="514" protocol="tcp")
    stop
}

# nginx: <= warning(4)
if ($programname == "nginx" and $syslogseverity <= 4) then {
    action(type="omfwd" target="192.168.1.100" port="514" protocol="tcp")
    stop
}

# mysqld: <= warning(4)
if ($programname == "mysqld" and $syslogseverity <= 4) then {
    action(type="omfwd" target="192.168.1.100" port="514" protocol="tcp")
    stop
}
```
```sh
# Enable:
systemctl restart rsyslog
# Testing:
logger -p auth.err "TEST-SSH-ERR from $(hostname)"
```

### NFS :
```sh
# Install & Enable NFS Service:
apt update
apt install nfs-kernel-server -y
mkdir -p /srv/log-archive
chown -R syslog:adm /srv/log-archive
echo '/srv/log-archive 192.168.1.100(rw,sync,no_subtree_check,root_squash)' | tee -a /etc/exports
exportfs -ra
systemctl restart nfs-kernel-server
```
```sh
# On Log Server: Mounting
apt install -y nfs-common
mkdir -p /mnt/log-archive
mount -t nfs4 192.168.1.200:/srv/log-archive /mnt/log-archive
# Permanent:
echo '192.168.1.200:/srv/log-archive /mnt/log-archive nfs4 rw,_netdev,noatime,nofail 0 0' | tee -a /etc/fstab
```

### Moving to NFS Script:
* This script will run after each rotation.
```sh
# /usr/local/bin/archive-logs-to-nfs.sh

#!/usr/bin/env bash
set -euo pipefail

SRC_BASE="/var/log/remote"
DST_BASE="/mnt/log-archive"

# Ensure NFS is mounted
if ! mountpoint -q "$DST_BASE"; then
  echo "WARN: $DST_BASE is not mounted, skipping archive move." >&2
  exit 0
fi

mkdir -p "$DST_BASE"

# Move .2.gz and older (keep current + .1 local)
for hostdir in "$SRC_BASE"/*; do
  [ -d "$hostdir" ] || continue
  host="$(basename "$hostdir")"
  mkdir -p "$DST_BASE/$host"

  # Find rotated gz files with index >= 2 for our services
  find "$hostdir" -maxdepth 1 -type f -regextype posix-extended \
    -regex '.*/(sshd|nginx|mysqld)\.log\.[2-9][0-9]*\.gz' -print0 |
  while IFS= read -r -d '' f; do
    # Preserve filename; place under per-host dir on NFS
    mv "$f" "$DST_BASE/$host/"
  done
done

# Optional: tighten perms on NFS side
chown -R syslog:adm "$DST_BASE" || true
chmod -R 0750 "$DST_BASE" || true
```
```sh
# Enable Scripts:
install -m 0750 /usr/local/bin/archive-logs-to-nfs.sh /usr/local/bin/archive-logs-to-nfs.sh
```

### Logrotate configuration:
```sh
# /etc/logrotate.d/remote-logs

# SSH logs: keep 7 days, rotate daily, compress, rotate also on size > 50M
/var/log/remote/*/sshd.log {
    daily
    rotate 7
    size 50M
    compress
    delaycompress
    missingok
    notifempty
    create 0640 syslog adm
    sharedscripts
    postrotate
        systemctl reload rsyslog >/dev/null 2>&1 || true
        /usr/local/bin/archive-logs-to-nfs.sh >/dev/null 2>&1 || true
    endscript
}

# Nginx logs: keep 14 days, rotate daily, compress, rotate also on size > 100M
/var/log/remote/*/nginx.log {
    daily
    rotate 14
    size 100M
    compress
    delaycompress
    missingok
    notifempty
    create 0640 syslog adm
    sharedscripts
    postrotate
        systemctl reload rsyslog >/dev/null 2>&1 || true
        /usr/local/bin/archive-logs-to-nfs.sh >/dev/null 2>&1 || true
    endscript
}

# MySQL logs: keep 30 days, rotate daily, compress, rotate also on size > 200M
/var/log/remote/*/mysqld.log {
    daily
    rotate 30
    size 200M
    compress
    delaycompress
    missingok
    notifempty
    create 0640 syslog adm
    sharedscripts
    postrotate
        systemctl reload rsyslog >/dev/null 2>&1 || true
        /usr/local/bin/archive-logs-to-nfs.sh >/dev/null 2>&1 || true
    endscript
}
```








