# BorgBackup

### Brief Introduction to BorgBackup (Borg)
> Borg is a lightweight, professional backup tool for Linux, known for its deduplication, compression, and end-to-end encryption features. Its goal is to let you create frequent, fast backups without unnecessarily filling up your disk space.

**Key Features**
* `Deduplication` : Only changed data blocks are stored, making subsequent backups smaller and faster.
* `Compression` : Supports efficient algorithms like lz4 and zstd for a balance of speed and size.
* `Encryption` : Client-side encryption with AES-256 and integrity verification (HMAC), making backups safe for both local and remote destinations.
* `High Performance` : Smart chunking and caching enable fast incremental backups.
* `Multiple Destinations` : Works with local disks, remote servers via SSH/SFTP, NAS devices, and more.

**Important Concepts**
* `Repository` : The storage location for all backups; can be local or remote.
* `Archive` : Each backup run creates a snapshot of your data at a specific point in time.
* `Chunking` : Files are split into smaller chunks to enable efficient deduplication.
* `Prune (Retention)` : Policies for keeping daily, weekly, or monthly backups to prevent disk overuse.
* `Compression` : Choose the right algorithm for your needs (e.g., lz4 for speed, zstd for higher compression).
* `Encryption Modes` : Options like repokey or keyfile define where keys are stored and how backups are recovered.


### Installing Borg:
```sh
sudo apt update
sudo apt install borgbackup
borg --version
```

### Create First Backup Repository:
```sh
# Create Directory:
mkdir -p /srv/borg
chown $USER:$USER /srv/borg
# Create Repository:
borg init --encryption=repokey /srv/borg
borg info /srv/borg # Show information of repository
```
* `--encryption=repokey` : Encryption Key will save in Repository
* `Passphrase` : Needed for Decryption of data

### First Backup Archive:
```sh
# Backup "/home/user/data" directory:
borg create /srv/borg::first-backup /home/user/data
borg list /srv/borg # List backup archives
borg list /srv/borg::first-backup # List content of Archive
```

### Test Restore:
```sh
# Restore archive content to "/tmp/restore":
mkdir -p /tmp/restore
borg extract /srv/borg::first-backup
```
```sh
# Restore specific file from an archive:
borg extract /srv/borg::first-backup path/to/file.txt
# Restore multiple files:
borg extract /srv/borg::first-backup data/file1.txt data/file2.txt
```

### Compression:

**Compression Algorithms:**

| Algorithm | Speed     | Final Size | Notes                                                  |
| --------- | --------- | ---------- | ------------------------------------------------------ |
| `none`    | Fastest   | None       | Only for testing or temporary backups                  |
| `lz4`     | Very fast | Medium     | Suitable for daily and quick backups                   |
| `zstd`    | Moderate  | Smaller    | Good balance between speed and compression             |
| `gzip`    | Slower    | Smaller    | Use when disk space is critical but speed is secondary |

```sh
borg create --compression zstd /srv/borg::second-backup /home/user/data
```

### Prune & Retention:
* `--keep-daily`
* `--keep-weekly`
* `--keep-monthly`
* `--keep-yearly`
* `--keep-within` : Version number

```sh
# Keep 7 daily & 4 weekly version: (Delete old versions)
borg prune -v --list /srv/borg --keep-daily=7 --keep-weekly=4 --prefix 'backup-'
```
* `-v --list` : Show details
* `--prefix` : Archives with specific name

### Mix Backup with Prune:
```sh
# Backup & Retention together:
borg create --compression zstd /srv/borg::backup-$(date +%Y-%m-%d) /home/user/data
borg prune -v --list /srv/borg --keep-daily=7 --keep-weekly=4 --prefix 'backup-'
```
* `backup-$(date +%Y-%m-%d)` : Archive name with date

### Remote Backup (SFTP):

```sh
# Create remote repository:
borg init --encryption=repokey user@remote-server:/srv/borg
# Backup on remote repository:
borg create --compression zstd user@remote-server:/srv/borg::backup-2025-08-21 /home/user/data
# Show remote archives:
borg list user@remote-server:/srv/borg
# Restore file from remote archive:
borg extract user@remote-server:/srv/borg::backup-2025-08-21 /home/user/data/file.txt
```

#### Using SFTP:
```sh
borg create --compression lz4 sftp://user@remote-server:/srv/borg::backup-2025-08-21 /home/user/data
```

### Backup from Docker Volumes & Containers:
```sh
# Backup from Docker Volumes:
docker run --rm -v my_volume:/data -v /home/user/data:/backup busybox tar czf /backup/my_volume.tar.gz /data
borg create /srv/borg::docker-volume-2025-08-21 /home/user/data/my_volume.tar.gz
```
```sh
# Backup from Container:
docker exec container_name tar czf - /app/data | borg create /srv/borg::container-2025-08-21 -
# Using for containers has no volume.
```

### Backup Automation using Cron:
```sh
# Simple daily script:
#!/bin/bash
# backup.sh

# Backup from Local Path:
borg create --compression zstd /srv/borg::backup-$(date +%Y-%m-%d) /home/user/data
# Prune old backups:
borg prune -v --list /srv/borg --keep-daily=7 --keep-weekly=4 --prefix 'backup-'
```
```sh
# Run job everyday at 02:00 AM:
0 2 * * * /home/user/backup.sh
```




