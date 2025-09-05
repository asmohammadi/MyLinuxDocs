# Backup(rsync, tar, cron)

### Rsync:
> `rsync` is backup tool which can check all files in subdirectories in the destination backup path and sync (replace) just the new files, without any versioning method.

```bash
# Backup from /home/user/data/ to /backup/data/ :
rsync -avh /home/user/data/ /backup/data/ # Extra files in backup path will keep.
rsync -avh --delete /home/user/data/ /backup/data/
rsync -avh --backup --backup-dir=/backup/old /home/user/data/ /backup/data/
rsync -avh --delete --backup --backup-dir=/backup/.old /source/ /backup/
rsync -avh --dry-run --log-file=/var/log/rsync-backup.log /home/user/data/ /backup/data/
# Using tar to keep old backups:
tar -czvf backup-$(date +%F).tar.gz /home/user/data/
```
* `-a` : Archive (Keep symlink, permissions, time, ... )
* `--delete` : Delete extra files in backup path.
* `--dry-run` : Show the result before running the backup.
* `--log-file=` : Make log file from the result.
* `--delete-before` : In backup path delete files older than the source.
* `--delete-during` : 
* `--backup-dir=` : Move files to another dir

### Tar (Archiving):

```bash
# Make archive backup from /home/user/data/ to a .tar.gz file in /backup/ path. 
tar -czvf /backup/data-backup-$(date +%F).tar.gz -C /home/user Data
```
* `-c` : Create
* `-z` : Gzip format
* `-f` : Output file name
* `data-backup-$(date +%F).tar.gz` : Archive file name with current time.
* `-C /home/user` : Change directory to /home/user before archive

```bash
tar -tzvf /backup/data-backup-$(date +%F).tar.gz
```
* `-t` : Show archive content.

```bash
tar -xzvf /backup/data-backup-2025-07-19.tar.gz -C /restore/location/
```
* `-x` : Extract archive file

### Backup Script with Rsync & Tar:

```bash
# Prepare for Backup:
# Source: /home/user/data/
# Destination: rsync: /backup/sync/
# Destination: tar: /backup/archive/
# Log path: /backup/logs/
mkdir -p /backup/sync /backup/archive /backup/logs
chmod +x backup.sh
```
```bash
#!/bin/bash

# 📅 Current time:
TODAY=$(date +%F)

# 📂 Paths:
SOURCE="/home/user/data/"
SYNC_DEST="/backup/sync/"
TAR_DEST="/backup/archive/data-backup-$TODAY.tar.gz"
LOGFILE="/backup/logs/rsync-$TODAY.log"

# ✅ Step One : Rsync with Log
rsync -avh --delete --log-file="$LOGFILE" "$SOURCE" "$SYNC_DEST"

# ✅ Step Two : Archive with Tar:
tar -czvf "$TAR_DEST" -C "$SOURCE" .

echo "Backup completed in $TODAY ✅"
```

### Cron:

```bash
crontab -e # Edit crontab
# Add this line:
0 2 * * * /path/to/backup.sh # Run Every day at 02:00 AM.
```

### Test Restore Backups:

```bash
# Restore archive to a custom path:
mkdir -p /restore_test
tar -xzvf /backup/archive/data-backup-2025-07-19.tar.gz -C /restore_test
```
```bash
# Restore archive to the source path:
rm -rf /home/user/data/
mkdir -p /home/user/data/
tar -xzvf /backup/archive/data-backup-2025-07-19.tar.gz -C /home/user/
```
```bash
# Restore Rsync Backup:
rsync -avh /backup/sync/ /home/user/data/
```








