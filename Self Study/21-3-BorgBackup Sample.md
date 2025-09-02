# BorgBackup Sample

### Scenario:
* server1 -> nginx service
* server2 -> mysql service
* server3 -> docker volumes
* nginx : Backup daily, keep 7 days
* Mysql : Backup weekly, keep 30 days
* Docker Volumes : Backup daily, keep last 3 versions

### Backup Structure:
```sh
/backups/
  ├── server1-nginx/
  ├── server2-mysql/
  ├── server3-docker/
```

### Repositories:
```sh
# Local Repositories:
borg init --encryption=repokey /backups/server1-nginx
borg init --encryption=repokey /backups/server2-mysql
borg init --encryption=repokey /backups/server3-docker
```
```sh
# Remote Repositories:
borg init --encryption=repokey user@backupserver:/backups/server1-nginx
borg init --encryption=repokey user@backupserver:/backups/server2-mysql
borg init --encryption=repokey user@backupserver:/backups/server3-docker
```

### Create Script:
```sh
# /usr/local/bin/borg-multi-backup.sh
#!/bin/bash

# Global Settings:
BORG_PASSPHRASE='YourSecurePass'
export BORG_PASSPHRASE

TIMESTAMP=$(date +'%Y-%m-%d_%H-%M')

# --- NGINX Backup ---
borg create --stats /backups/server1-nginx::nginx-$TIMESTAMP /var/log/nginx
borg prune --keep-daily=7 --keep-weekly=0 /backups/server1-nginx

# --- MYSQL Backup ---
mysqldump -u root -pYourPassword --all-databases > /tmp/mysql_backup.sql
borg create --stats /backups/server2-mysql::mysql-$TIMESTAMP /tmp/mysql_backup.sql
rm /tmp/mysql_backup.sql
borg prune --keep-weekly=4 --keep-daily=0 /backups/server2-mysql

# --- Docker Volumes Backup ---
borg create --stats /backups/server3-docker::docker-$TIMESTAMP /var/lib/docker/volumes
borg prune --keep-last=3 /backups/server3-docker
```
```sh
chmod +x /usr/local/bin/borg-multi-backup.sh
```

### Automate backup using Cron:
```sh
crontab -e
# Run everyday at 02:00 AM:
0 2 * * * /usr/local/bin/borg-multi-backup.sh >> /var/log/borg-multi-backup.log 2>&1
```

## Advance Backup Script:

### Create Backup Config Script:
```sh
# backup_config.sh

# Repositories for each server:
declare -A REPOS=(
  ["web1"]="user@web1:/backups/borg/web1"
  ["db1"]="user@db1:/backups/borg/db1"
  ["app1"]="user@app1:/backups/borg/app1"
)

# Paths to backup:
declare -A PATHS=(
  ["web1"]="/var/www /etc/nginx"
  ["db1"]="/var/lib/mysql /etc/mysql"
  ["app1"]="/opt/apps /etc/systemd"
)

# Filters (Excluding some paths from backup):
declare -A EXCLUDES=(
  ["web1"]="--exclude /var/www/cache"
  ["db1"]="--exclude /var/lib/mysql/tmp"
  ["app1"]=""
)

# Backup Retentions:
declare -A RETENTION=(
  ["web1"]="--keep-daily=7 --keep-weekly=4 --keep-monthly=6"
  ["db1"]="--keep-daily=14 --keep-weekly=8 --keep-monthly=12"
  ["app1"]="--keep-daily=7 --keep-weekly=4 --keep-monthly=6"
)

# Logs Path:
LOG_FILE="/var/log/borg/backup_$(date +%F).log"
```

### Backup Script:
```sh
# multi_backup.sh
#!/bin/bash
source ./backup_config.sh

echo "===== Backup started at $(date) =====" | tee -a "$LOG_FILE"

for SERVER in "${!REPOS[@]}"; do
    echo ">>> Processing $SERVER ..." | tee -a "$LOG_FILE"

    REPO=${REPOS[$SERVER]}
    PATH=${PATHS[$SERVER]}
    EXCLUDE=${EXCLUDES[$SERVER]}
    RETENTION_RULES=${RETENTION[$SERVER]}

    # Create archive with server name & timestamp:
    borg create --verbose --stats --progress \
        "$REPO"::"$SERVER-$(date +%F_%H-%M)" \
        $PATH $EXCLUDE 2>&1 | tee -a "$LOG_FILE"

    if [ ${PIPESTATUS[0]} -eq 0 ]; then
        echo "[OK] Backup for $SERVER completed successfully." | tee -a "$LOG_FILE"
    else
        echo "[ERROR] Backup for $SERVER failed!" | tee -a "$LOG_FILE"
        continue
    fi

    # Prune old backups:
    borg prune --verbose "$REPO" $RETENTION_RULES 2>&1 | tee -a "$LOG_FILE"
    echo ">>> Retention applied for $SERVER" | tee -a "$LOG_FILE"

    # Compress & Archive health:
    borg compact --verbose "$REPO" 2>&1 | tee -a "$LOG_FILE"
done

echo "===== Backup finished at $(date) =====" | tee -a "$LOG_FILE"
```

### Automate Backup using Cron:
```sh
# Run everyday at 02:00 AM:
0 2 * * * /root/scripts/multi_backup.sh
```




