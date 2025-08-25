# 31-Disk Management

**lsblk:**
> Will show all disks in OS.
```bash
root@server:~# lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                         8:0    0   60G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0    2G  0 part /boot
└─sda3                      8:3    0   58G  0 part
  └─ubuntu--vg-ubuntu--lv 252:0    0   29G  0 lvm  /
sdb                         8:16   0   50G  0 disk
sr0                        11:0    1 1024M  0 rom

root@server:~# ls /dev/sd*
/dev/sda  /dev/sda1  /dev/sda2  /dev/sda3  /dev/sdb
```

### Steps for adding a Disk:
* Create Partition
* Make FileSystem
* Mounting


#### Creating Partition:

**fdisk:**
> `fdisk` also known as format disk is a dialog-driven command in Linux used for creating and manipulating disk partition table. It is used for the view, create, delete, change, resize, copy and move partitions on a hard drive.

```bash
fdisk -l # Show disks
```
```bash
root@server:~# fdisk -l
Disk /dev/sdb: 50 GiB, 53687091200 bytes, 104857600 sectors
Disk model: VMware Virtual S
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

Disk /dev/sda: 60 GiB, 64424509440 bytes, 125829120 sectors
Disk model: VMware Virtual S
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: C150632E-755A-440F-910E-704227E98418

Device       Start       End   Sectors Size Type
/dev/sda1     2048      4095      2048   1M BIOS boot
/dev/sda2     4096   4198399   4194304   2G Linux filesystem
/dev/sda3  4198400 125827071 121628672  58G Linux filesystem

Disk /dev/mapper/ubuntu--vg-ubuntu--lv: 29 GiB, 31134318592 bytes, 60809216 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```
```bash
root@server:~# fdisk /dev/sdb

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0xbd67d3c2.

Command (m for help): m

Help:

  DOS (MBR)
   a   toggle a bootable flag
   b   edit nested BSD disklabel
   c   toggle the dos compatibility flag

  Generic
   d   delete a partition
   F   list free unpartitioned space
   l   list known partition types
   n   add a new partition
   p   print the partition table
   t   change a partition type
   v   verify the partition table
   i   print information about a partition

  Misc
   m   print this menu
   u   change display/entry units
   x   extra functionality (experts only)

  Script
   I   load disk layout from sfdisk script file
   O   dump disk layout to sfdisk script file

  Save & Exit
   w   write table to disk and exit
   q   quit without saving changes

  Create a new label
   g   create a new empty GPT partition table
   G   create a new empty SGI (IRIX) partition table
   o   create a new empty DOS partition table
   s   create a new empty Sun partition table


Command (m for help): 
```
**Steps for creating Partition:**
```bash
fdisk -l /dev/sdb
fdisk /dev/sdb
m # Help Menu
n # New Partition
p/e # Partition Type (Primary/Extended)
1-4 # Partition Number (3 Primary, 1 Extended)
2048 # Size of partition (First sector/Default)
+5G # Size of partition (Last sector)
# Created 1 partition of type Linux & size of 5Gb.
n # New Partition (Adding Logical Volume)
p # Print

Command (m for help): p

Device     Boot    Start       End  Sectors Size Id Type
/dev/sdb1           2048  10487807 10485760   5G 83 Linux
/dev/sdb2       10487808  31459327 20971520  10G 83 Linux
/dev/sdb3       31459328  37750783  6291456   3G 83 Linux
/dev/sdb4       37750784 104857599 67106816  32G  5 Extended
/dev/sdb5       37752832  58724351 20971520  10G 83 Linux

w # Write & Exit (Apply changes)
```
```bash
root@server:~# fdisk -l /dev/sdb
Disk /dev/sdb: 50 GiB, 53687091200 bytes, 104857600 sectors
Disk model: VMware Virtual S
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x6b7aef3c

Device     Boot    Start       End  Sectors Size Id Type
/dev/sdb1           2048  10487807 10485760   5G 83 Linux
/dev/sdb2       10487808  31459327 20971520  10G 83 Linux
/dev/sdb3       31459328  37750783  6291456   3G 83 Linux
/dev/sdb4       37750784 104857599 67106816  32G  5 Extended
/dev/sdb5       37752832  58724351 20971520  10G 83 Linux
```
```bash
root@server:~# lsblk
NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda                         8:0    0   60G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0    2G  0 part /boot
└─sda3                      8:3    0   58G  0 part
  └─ubuntu--vg-ubuntu--lv 252:0    0   29G  0 lvm  /
sdb                         8:16   0   50G  0 disk
├─sdb1                      8:17   0    5G  0 part
├─sdb2                      8:18   0   10G  0 part
├─sdb3                      8:19   0    3G  0 part
├─sdb4                      8:20   0    1K  0 part
└─sdb5                      8:21   0   10G  0 part
sr0                        11:0    1 1024M  0 rom
```
**Steps to change partition type:**
```bash
fdisk /dev/sdb
t # Change partition type
1-6 # Select partition by number
L # List partition types
8e # Hex/Alias (Linux LVM Type)
# Change type of partition from "Linux" to "Linux LVM".
w # Write & Exit (Apply changes)
```

**gdisk:**
> `Gdisk` is GPT fdisk for managing GPT Partitions. It will automatically convert an old-style Master Boot Record (MBR) partition table  to the newer Globally Unique Identifier (GUID) Partition Table (GPT) format.

```bash
root@server:~# gdisk /dev/sda
GPT fdisk (gdisk) version 1.0.10

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.

root@server:~# gdisk /dev/sdb
GPT fdisk (gdisk) version 1.0.10

Partition table scan:
  MBR: MBR only
  BSD: not present
  APM: not present
  GPT: not present

***************************************************************
Found invalid GPT and valid MBR; converting MBR to GPT format
in memory. THIS OPERATION IS POTENTIALLY DESTRUCTIVE! Exit by
typing 'q' if you don't want to convert your MBR partitions
to GPT format!
***************************************************************
```



