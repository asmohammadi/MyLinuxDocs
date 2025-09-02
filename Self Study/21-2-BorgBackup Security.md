# BorgBackup Security

### Types of Key:
* `none` 
* `repokey` : Default mode, save in Repository.
* `keyfile` : Key will save in local system.
* `repokey-blake2` : Key will save in Repository, but faster & more secure.
* `keyfile-blake2` : Key will save in local system, but faster & the most secure.

### Create Secure Repository:
```sh
borg init --encryption=repokey /path/to/repo
borg init --encryption=repokey-blake2 /path/to/repo
borg init --encryption=keyfile-blake2 /mnt/backup/server-backup
borg key list /mnt/backup/server-backup # Show key information
```

### Backup from keys:
```sh
cp ~/.config/borg/keys/* /media/usb/ # In keyfile mode
borg key export /mnt/backup/server-backup ./server-backup-key.txt
```


