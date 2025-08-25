# 37-NFS

> `NFS` (Network File System) is a distributed file system protocol that allows clients to access files and directories on remote servers over a network. It enables file sharing between machines in a network, allowing multiple users to access and modify files as if they were on their local system.

#### Installing NFS Server:

**Server side:**
```bash
# Install NFS Server:
sudo apt install nfs-kernel-server nfs-common 
```
```bash
# Create a shared directory:
mkdir /mnt/nfs
chown nobody:nogroup /mnt/nfs
chmod 777 /mnt/nfs
```
```bash
# Add directory to the /etc/exports file:
echo "/Directory/Path    ClientsIPAddress(rw,sync,no_subtree_check)" >> /etc/exports
echo "/Directory/Path    *(rw,sync,no_subtree_check)" >> /etc/exports
# Example:
echo "/mnt/nfs    192.168.1.0/24(rw,sync,no_subtree_check)" >> /etc/exports
```
```bash
# restart NFS Service:
exportfs -r
exportfs -a
sudo systemctl restart nfs-kernel-server
```

**Client side:**
```bash
# Install NFS Client:
sudo apt update
sudo apt install nfs-common
```
```bash
# Create a directory:
mkdir /mnt/nfs
chown nobody:nogroup /mnt/nfs
chmod 777 /mnt/nfs
```
```bash
# Mount NFS shared from server:
mount NFSServerIP:/SharedDirectory/Path /Directory/Path
# example:
mount 192.168.1.180:/mnt/nfs /mnt/nfs
```
```bash
# Add directory to /etc/fstab:
echo "NFSServerIP:SharedDirectory/Path /Directory/Path nfs defaults 0 0" >> /etc/fstab
# Example:
echo "192.168.1.180:/mnt/nfs /mnt/nfs nfs defaults 0 0" >> /etc/fstab
```




