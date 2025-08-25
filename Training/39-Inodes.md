# 39-Inodes

**df:**
```bash
df -th # Show disk free space on filesystems
```
* `-T` : Display Filesystem's Type
* `-t` : Display specific filesystem type
* `-h` : Display size in Human-readable
* `-i` : Display iNodes Information in Filesystems
* `-x` : Exclude specific Filesystem Type
* `-a` : Display all information
* `-K`/`-M`/`-G` : Display size in Kilobyte/Megabyte/Gigabyte
```bash
root@ubuntu16-1:~# df -Th

Filesystem     Type      Size  Used Avail Use% Mounted on
udev           devtmpfs  452M     0  452M   0% /dev
tmpfs          tmpfs      97M  6.4M   90M   7% /run
/dev/sda1      ext4       49G  5.4G   41G  12% /
tmpfs          tmpfs     481M  284K  481M   1% /dev/shm
tmpfs          tmpfs     5.0M  4.0K  5.0M   1% /run/lock
tmpfs          tmpfs     481M     0  481M   0% /sys/fs/cgroup
tmpfs          tmpfs      97M   48K   97M   1% /run/user/1001
```

```bash
root@ubuntu16-1:~# df -i

Filesystem      Inodes  IUsed   IFree IUse% Mounted on
udev            115699    456  115243    1% /dev
tmpfs           123135    750  122385    1% /run
/dev/sda1      3211264 256212 2955052    8% /
tmpfs           123135      9  123126    1% /dev/shm
tmpfs           123135      6  123129    1% /run/lock
tmpfs           123135     17  123118    1% /sys/fs/cgroup
tmpfs           123135     27  123108    1% /run/user/1001
```

**du:**
> Disk Usage used for Files and Directories.
```bash
du
du -sh
du -ah
```
* `-a` : Write count of all files not just directories (Show hidden directory or file)
* `-h` : Display size in human-readable
* `-s` : Display only total size for each directory
```bash
root@ubuntu16-1:~# du -sh

6.5M	/etc
1.5G    /mnt
40K     /home
4.0K    /opt
0       /dev
0       /lib
3.9G    /swap.img
2.4G    /usr
64K     /tmp
```

**fsck:**
> `fsck` is the main tool for checking and repairing filesystems.

```bash
root@ubuntu16-1:~# fsck
fsck          fsck.ext3     fsck.fat      fsck.nfs      
fsck.cramfs   fsck.ext4     fsck.minix    fsck.vfat     
fsck.ext2     fsck.ext4dev  fsck.msdos 

root@ubuntu16-1:~# ls /sbin/fsck*
/sbin/fsck         /sbin/fsck.ext3     /sbin/fsck.fat    /sbin/fsck.nfs
/sbin/fsck.cramfs  /sbin/fsck.ext4     /sbin/fsck.minix  /sbin/fsck.vfat
/sbin/fsck.ext2    /sbin/fsck.ext4dev  /sbin/fsck.msdos
```
> Some of these are just links to e2fsck command and they are the same
```bash
root@ubuntu16-1:~# fsck /dev/sda1

fsck from util-linux 2.27.1
e2fsck 1.42.13 (17-May-2015)
/dev/sda1 is mounted.
e2fsck: Cannot continue, aborting.
```

> **In order to use fsck the partition should be unmounted, otherwise it might cause damages!**

```bash
# Lets simply check file system on an unmounted ext3 partition (sdb1) and try to fix errors:

root@ubuntu16-1:~# fsck /dev/sdb1

fsck from util-linux 2.27.1
e2fsck 1.42.13 (17-May-2015)
/dev/sdb1: clean, 11/1310720 files, 126322/5242624 blocks
```
 This command will attempt to check **/dev/sdb1**, and report any errors it finds.The exit code returned by fsck is one of following conditions:

* 0 No errors 
* 1 Filesystem errors corrected 
* 2 System should be rebooted 
* 4 Filesystem errors left uncorrected 
* 8 Operational error 
* 16 Usage or syntax error 
* 32 Checking canceled by user request 
* 128 Shared-library error

* `-N` option just shows what would be executed but do not attempt to repair them:
```bash
root@ubuntu16-1:~# fsck -N /dev/sdb1

fsck from util-linux 2.27.1
[/sbin/fsck.ext3 (1) -- /dev/sdb1] fsck.ext3 /dev/sdb1
```

* `-n ` causes these commands not to fix anything and just show what was going to be done:
```bash
root@ubuntu16-1:~# fsck -n /dev/sdb1

fsck from util-linux 2.27.1
e2fsck 1.42.13 (17-May-2015)
/dev/sdb1: clean, 11/1310720 files, 126322/5242624 blocks
```

Normally, `fsck` will skip parts of the filesystem marked as "clean" — meaning all pending writes were successfully made. The `-f` (force) option specifies that `fsck` should check parts of the filesystem even if they are not "dirty". The result is a less efficient, but a more thorough check.
```bash
root@ubuntu16-1:~# fsck -f /dev/sdb1

fsck from util-linux 2.27.1
e2fsck 1.42.13 (17-May-2015)
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
/dev/sdb1: 11/1310720 files (0.0% non-contiguous), 126322/5242624 blocks
```
```bash
fsck -M /dev/sda1 # Prevents running fsck on mounted filesystem.
fsck -t ext3 /dev/sdb1 # Check Only a Specific Filesystem Type.
fsck -y -f /dev/sdb1 # Pass “yes” to all the questions to fix.
```
> For checking  a XFS filesystem, we have to use xfs_check command

### Tools for check & repair for `EXT` Filesystems:

* `tune2fs` : Adjusts parameters on ext2 and ext3 filesystems and can set journaling.
* `dumpe2fs` : Prints the super block and block group descriptor information for an ext2 or ext3 filesystem.
* `debugfs` : Is an interactive filesystem debugger. Use it to examine or change the state of an ext2 or ext3 filesystem.

### Tools for check & repair for `ReiserFS` Filesystem:

* `reiserfstune` : Displays and adjusts parameters on ReiserFS filesystems.
* `debugreiserfs` : Performs similar functions to dumpe2fs and debugfs for ReiserFS filesystems.

### Tools for check & repair for `XFS` Filesystem:

* `xfs_info` : Displays XFS filesystem information.
* `xfs_growfs` : Expands an XFS filesystem.
* `xfs_admin` : Changes the parameters of an XFS filesystem.
* `xfs_repair` : Repairs an XFS filesystem when the mount checks are not sufficient to repair the system.
* `xfs_db  ` : Examines or debugs an XFS filesystem.

### Tools for check & repair for `BTRFS` Filesystem:

* `btrfs` : Displays many aspects of btrfs filesystem information.
* `btrfsck` : Check btrfs filesystems.
* `btrfs-find-root` : Finds the block that is the root of the btrfs filesystem.
* `btrfs-debug-tree` : Displays btrfs internal metadata.
* `btrfstune` : Tune various btrfs filesystem parameters, and enables or disables some extended features.
* `btrfs-restore` : Attempt to restore files from a damaged btrfs filesystem.

**watch:**
```bash
watch -d -n 1 Command # Run the command and show differences in every one second.
watch -d -n 1 df -i
```
* `-d` : Show differences
* `-n` : Set time


