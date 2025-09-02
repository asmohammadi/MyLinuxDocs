# Restic Backup

### Installing Restic:
```sh
apt update
apt install restic
restic version
```

### Create Repository:
```sh
# Create local repository:
mkdir -p /backup/restic_repo
restic init --repo /backup/restic_repo
# Asking for a Password.
```

### Backup:
```sh
# Backup from "/etc/"
restic -r /backup/restic_repo backup /etc
```

### Check Backup:
```sh
restic -r /backup/restic_repo snapshots
```

### Restore Backup:
```sh
mkdir /restore
restic -r /backup/restic_repo restore latest --target /restore
# Restore a specific file:
restic restore latest --target /tmp/restore-test --include "/etc/nginx/nginx.conf"

```

### Remote Backup (SFTP/SSH):
```sh
# Create Remote Repository:
restic -r sftp:user@remote-server:/path/to/repo init
# Variables:
export RESTIC_REPOSITORY="sftp:backupuser@192.168.1.100:/data/backups/project1"
export RESTIC_PASSWORD="StrongPassword123"

restic init
```
```sh
# Create Remote Backup:
restic -r sftp:backupuser@192.168.1.100:/data/backups/project1 backup /var/www
# Variables:
export RESTIC_REPOSITORY="sftp:backupuser@192.168.1.100:/data/backups/project1"
export RESTIC_PASSWORD="StrongPassword123"

restic backup /var/www /etc/nginx
```
```sh
# Display Backups list:
restic snapshots
```



