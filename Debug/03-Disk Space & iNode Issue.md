# Disk Space & iNode Issue:

```sh
df -h
du -sh 
du -sh /var/log # nginx_access.log
rm -rf /var/log/nginx/access.log
df -h # Disk space has no change
du -sh /var/log # Show nothing
df -h # Display partition size based on metadata of files
ls -il /var/log/nginx # Display items with iNode
lsof | less # Show open files & process & iNodes
lsof | grep -i delete # Display deleted files with size & iNode (iNode will keep after removing files)
systemctl reload nginx
# The Nginx master PID will keep but the workers process ID will change
lsof | grep -i delete # The deleted files & iNode now removed.
df -h # Disk space has been freed
```
```sh
# Better solution: Keep a backup from log file & free more space on disk
mv /var/log/nginx/access.log access.log.bak; systemctl reload nginx
tar cvf access.log.tar access.log.bak
rm -rf access.log.bak
```














