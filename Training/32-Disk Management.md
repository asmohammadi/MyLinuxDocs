# 32-Disk Management

#### Make FileSystem:

**FileSystem:**
> `FileSystem` is a layer which is under the operating system that handles the positioning of your data on the storage.
> Linux supports several different file systems:

    Ext, Ext2, Ext3, Ext4, JFS, XFS, btrfs and swap

**mkfs:**
```bash
mkfs # Make FileSystem
mkfs.ext4
mkfs -t ext4
mkfs.ext4 /dev/sdb2
mkfs -t ext4 /dev/sdb2
mkfs -t ext4 -L DATA /dev/sdb2
mkfs -t xfs -i size=1024 /dev/sdb3
```
* **`-t` : Partition Type**
* **`-L` : Partition Label**
* **`-i` : Larger inode (Normal is 512)**


```bash
root@server:~# mkfs

mkfs         mkfs.btrfs   mkfs.ext2    mkfs.ext4    mkfs.minix   mkfs.ntfs    mkfs.xfs
mkfs.bfs     mkfs.cramfs  mkfs.ext3    mkfs.fat     mkfs.msdos   mkfs.vfat

root@server:~# ls /sbin/mkfs.*

/sbin/mkfs.bfs    /sbin/mkfs.cramfs  /sbin/mkfs.ext3  /sbin/mkfs.fat    /sbin/mkfs.msdos  /sbin/mkfs.vfat
/sbin/mkfs.btrfs  /sbin/mkfs.ext2    /sbin/mkfs.ext4  /sbin/mkfs.minix  /sbin/mkfs.ntfs   /sbin/mkfs.xfs
```
```bash
root@server:~# mkfs -t ext4 /dev/sdb2

mke2fs 1.47.0 (5-Feb-2023)
Creating filesystem with 2621440 4k blocks and 655360 inodes
Filesystem UUID: 93bc7979-4a9d-4519-b3f4-2096fc90f9b3
Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done
Writing inode tables: done
Creating journal (16384 blocks): done
Writing superblocks and filesystem accounting information: done
```
```bash
root@server:~# mkfs.xfs /dev/sdb3

meta-data=/dev/sdb3              isize=512    agcount=4, agsize=196608 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=1
         =                       reflink=1    bigtime=1 inobtcount=1 nrext64=0
data     =                       bsize=4096   blocks=786432, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=16384, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
```

**blkid:**
```bash
blkid # Show FileSystem, Type, Block size and UUID of partitions.

root@server:~# blkid

/dev/mapper/ubuntu--vg-ubuntu--lv: UUID="9efb1456-97cd-47c4-9f23-e68efa8c28c8" BLOCK_SIZE="4096" TYPE="ext4"
/dev/sda2: UUID="006d631a-140b-4696-a637-ccdcfeeb6290" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="15bb2700-4725-40a0-add4-2a390da57158"
/dev/sda3: UUID="Yk9ySD-gUK5-twZy-7c1x-f0F0-9weP-nqdc4d" TYPE="LVM2_member" PARTUUID="d9c71412-79e3-48a6-8013-dd7de4b79f30"
/dev/sdb2: UUID="93bc7979-4a9d-4519-b3f4-2096fc90f9b3" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="6b7aef3c-02"
/dev/sdb3: UUID="783e6c06-c2a7-4bce-b9c0-e6ef5cea2eac" BLOCK_SIZE="512" TYPE="xfs" PARTUUID="6b7aef3c-03"
/dev/sdb5: PARTUUID="6b7aef3c-05"
/dev/sdb1: PARTUUID="6b7aef3c-01"
/dev/sda1: PARTUUID="f5078db8-2151-44f2-8ebf-8f853a431046"
```

**mkswap:**
> `Mkswap` will make Swap space. First need to create a Swap Partition with type 82 (Linux Swap).

```bash
mkswap /dev/sdb1

root@ubuntu16-1:/# mkswap /dev/sdb1

mkswap: /dev/sdb1: warning: wiping old ext3 signature.
Setting up swapspace version 1, size = 20 GiB (21473783808 bytes)
no label, UUID=0dcd7e90-4b45-4d5f-808c-320f1e5ba8a3
```

#### Mounting created partitions:

**mount:**
```bash
mount Partition/Path MountPoint/Directory/ # Mounting a Device to a Directory (Temporary)
mount /dev/sdb1 /DATA_SDB1/
umount /dev/sdb1 # UnMount SDB1
```
```bash
root@server:~# mkdir /DATA_SDB1
root@server:~# mount /dev/sdb1 /DATA_SDB1/
root@server:~# lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                         8:0    0   60G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0    2G  0 part /boot
└─sda3                      8:3    0   58G  0 part
  └─ubuntu--vg-ubuntu--lv 252:0    0   29G  0 lvm  /
sdb                         8:16   0   50G  0 disk
├─sdb1                      8:17   0    5G  0 part /DATA_SDB1
├─sdb2                      8:18   0   10G  0 part
├─sdb3                      8:19   0    3G  0 part
├─sdb4                      8:20   0    1K  0 part
└─sdb5                      8:21   0   10G  0 part
sr0                        11:0    1 1024M  0 rom
```

**/etc/fstab:**
> `fstab` will use for **permanent** mounting, using Partition Label or UUID. 

```bash
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/ubuntu-vg/ubuntu-lv during curtin installation
/dev/disk/by-id/dm-uuid-LVM-ozSGyXSleT7209Id7lavAG9mwqqmpdDOfvN6JaY1l2URedPBspHloKEBjIYtTSe7 / ext4 defaults 0 1
# /boot was on /dev/sda2 during curtin installation
/dev/disk/by-uuid/006d631a-140b-4696-a637-ccdcfeeb6290 /boot ext4 defaults 0 1
/swap.img       none    swap    sw      0       0
/dev/sdb1 /DATA_SDB1 ext4 defaults 0 1
/dev/disk/by-uuid/93bc7979-4a9d-4519-b3f4-2096fc90f9b3 /DATA_SDB2 ext4 defaults 0 1

~
```
```bash
mount -a # Mounting devices added to /etc/fstab automatically.
systemctl deamon-reload
```
```bash
root@server:~# ls -l /dev/disk/by-uuid/

total 0
lrwxrwxrwx 1 root root 10 Jun 11 13:33 006d631a-140b-4696-a637-ccdcfeeb6290 -> ../../sda2
lrwxrwxrwx 1 root root 10 Jun 12 13:45 66a727df-df4b-49ad-833c-0384e4661ada -> ../../sdb1
lrwxrwxrwx 1 root root 10 Jun 12 08:36 783e6c06-c2a7-4bce-b9c0-e6ef5cea2eac -> ../../sdb3
lrwxrwxrwx 1 root root 10 Jun 12 08:20 93bc7979-4a9d-4519-b3f4-2096fc90f9b3 -> ../../sdb2
lrwxrwxrwx 1 root root 10 Jun 11 13:33 9efb1456-97cd-47c4-9f23-e68efa8c28c8 -> ../../dm-0
lrwxrwxrwx 1 root root 10 Jun 12 13:46 f25b4888-b0a8-4f3c-8c85-6ac65e87c550 -> ../../sdb5
```

