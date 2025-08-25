# Linux Basics

## FileSystem, Basic Commands, Users & Groups:

### FileSystem Hierarchy:

- `/`	            => Filesystem Root
- `/bin`	        => دستورات اجرایی پایه (مثل ls, cp, mv)
- `/sbin`	        => دستورات اجرایی برای مدیر سیستم (مثل reboot, iptables)
- `/etc`	        => فایل‌های پیکربندی سیستم (Configuration Files)
- `/home`	        => پوشه‌ی Home کاربران 
- `/root`	        => پوشه‌ی Home کاربر root
- `/var`	        => فایل‌های متغیر مثل لاگ‌ها، صف پرینت، کش‌ها
- `/usr`	        => نرم‌افزارهای نصب‌شده توسط کاربر و فایل‌های share شده
- `/tmp`	        => Temporary Files
- `/dev`	        => فایل‌های دستگاه (Device Files  مثل sda, tty)
- `/proc`	        => اطلاعات لحظه‌ای از کرنل و پردازش‌ها (Virtual Filesystem)
- `/sys`	        => اطلاعات و تنظیمات سخت‌افزاری سیستم
- `/opt`	        => محل نصب نرم‌افزارهای third-party (مثلاً Chrome)
- `/media` `/mnt`	=> Mountpoint برای External Device ها (USB, CD, etc.)


### Basic commands:
```bash
pwd
ls
ls -l
cd
cd ~ # Back to Home directory
du # Disk Usage
du -h
du -h --max-depth=1 / # Disk Usage of each directory in "/".
df # Disk Free Space
df -h
find /etc -name "ssh*" # Searching files
cat /etc/os-release
```

### Users & Groups:
```bash
whoami # Current User
id # Current User Information
cut -d: -f1 /etc/passwd # List all Users.
cut -d: -f1 /etc/group # List all Groups
adduser testuser # Create New User
usermod -aG sudo testuser # Add a User to sudo Group.
groups testuser # Display Group Membership of a User.
deluser testuser # Remove a User
deluser --remove-home testuser # Remove User include Home directory
addgroup devteam # Create New Group
usermod -aG devteam testuser # Add a User to the New Group
```

### Permissions:
```bash
ls -l # Show file & directory permissions
-rw-r--r-- 1 user group 1234 Jul 13 14:00 example.txt

sudo chown user:group filename # Change file's owner

chmod u+x filename     # Set execution permision for User Owner
chmod g-w filename     # Remove Write permission for Group
chmod o=r filename     # Set just Read-only permission for Others
```

#### Permissions in Numeric mode:

* `rwx` : 7
* `rw-` : 6
* `r-x` : 5
* `r--` : 4
* `-wx` : 3
* `-w-` : 2
* `--r` : 1
* `---` : 0

```bash
# Examples:
chmod 755 script1.sh  # rwxr-xr-x
chmod 644 notes.txt    # rw-r--r--
```
```bash
chmod -R 755 dir1/ # Set permission recursive.
```

## Services & Boot Process Management with Systemd

### systemd:
> New modern init system in Linux
> Controlling start, stop and service management, logging and boot process.

```bash
systemctl status servicename
systemctl start servicename
systemctl stop servicename
systemctl restart servicename
systemctl enable servicename
systemctl disable servicename
systemctl is-enabled servicename # Checking service in boot process.
systemctl list-units --type=service # Display enabled services
systemctl list-units --type=service --all # Display all services
```

### Target in SystemD:
> Old Linux OS -> RunLevel (SysVinit)
> New Linux OS -> Target (In SystemD)

#### Important Targets:
```bash
graphical.target # Graphical complete boot
multi-user.target # Multi-user without GUI (Servers)
rescue.target # Recovery mode with minimum services
emergency.target # Emergency mode just with Root without any service
default.target # Default Target
```
```bash
# Target commands:
systemctl get-default # Show current target
systemctl set-default multi-user.target # Set default target
systemctl isolate rescue.target # Switch target without reboot (Entering Rescue mode)
systemctl list-units --type=target # Display active targets
systemctl list-units --type=target --all # Display all targets
```
```bash
systemctl list-units --type=target # Active targets

  UNIT                    LOAD   ACTIVE SUB    DESCRIPTION
  basic.target            loaded active active Basic System
  bluetooth.target        loaded active active Bluetooth Support
  cryptsetup.target       loaded active active Local Encrypted Volumes
  getty-pre.target        loaded active active Preparation for Logins
  getty.target            loaded active active Login Prompts
  graphical.target        loaded active active Graphical Interface
  integritysetup.target   loaded active active Local Integrity Protected Volumes
  local-fs-pre.target     loaded active active Preparation for Local File Systems
  local-fs.target         loaded active active Local File Systems
  multi-user.target       loaded active active Multi-User System
  network-online.target   loaded active active Network is Online
  network-pre.target      loaded active active Preparation for Network
  network.target          loaded active active Network
  nss-lookup.target       loaded active active Host and Network Name Lookups
  paths.target            loaded active active Path Units
  remote-fs-pre.target    loaded active active Preparation for Remote File Systems
  remote-fs.target        loaded active active Remote File Systems
  slices.target           loaded active active Slice Units
  snapd.mounts-pre.target loaded active active Mounting snaps
  snapd.mounts.target     loaded active active Mounted snaps
  sockets.target          loaded active active Socket Units
  sound.target            loaded active active Sound Card
  swap.target             loaded active active Swaps
  sysinit.target          loaded active active System Initialization
  time-set.target         loaded active active System Time Set
  timers.target           loaded active active Timer Units
  veritysetup.target      loaded active active Local Verity Protected Volumes
```

### Logging with Journalctl:
> SystemD will save services and system logs in `journal` structure.

```bash
journalctl # Display all logs
journalctl -f # Realtime logs (tail -f)
journalctl -u ssh # Display logs of a Service
journalctl -b # Display logs from last Boot
journalctl --since "2025-07-13" --until "2025-07-13 15:00" # Display logs with date
journalctl --list-boots # Display reboot logs
journalctl -b -1 # Display last boot logs
journalctl | grep -i error # Search a key word in logs
```

## Apt & Package Management

### Apt:
```bash
# Apt important Paths:
/etc/apt/sources.list # Repository files
/etc/apt/sources.list.d/ # Extra repository files
/var/cache/apt/archives # Downloaded packages cache
/var/log/apt/ # Apt activity Logs
```

### Apt Commands:
```bash
apt update # Update the list of packages in repositories
apt upgrade # Upgrade installed packages
apt install Package
apt remove Package # Remove binaries & executive files (Not configurations)
apt purge Package # Remove with all configurations
apt autoremove # Remove dependent files.
apt clean # Remove the cache of uninstalled apps.
```

### Repositories:
```bash
# Repositories Path:
/etc/apt/sources.list # Repository files
/etc/apt/sources.list.d/ # Extra repository files
```

**Structure of Repositories:**
```
deb http://archive.ubuntu.com/ubuntu focal main restricted universe multiverse
```
* `deb` : Type of repository
* `URL` : Server of the repository
* `focal` : Distribution (Ubuntu 20.04)
* `main restricted universe multiverse` : Sections

> Any changes to Repositories Lists need `apt update` command.

### Cache Management & Cleanup:

```bash
apt clean # Remove all .deb files stored in "/var/cache/apt/archives/" path.
apt autoremove # Remove dependent files.
```
```bash
# Troubleshoot:
Could not get lock /var/lib/dpkg/lock-frontend
# Solution:
rm /var/lib/dpkg/lock-frontend
dpkg --configure -a # Reconfigure the package
```
```bash
apt install -f # Fix broken dependencies
```

## Search & Manage Files with Find & Xargs

### Find Structure:

```bash
# Structure:
find [Searching source] [Conditions] [Operational options]
find /home -name test.txt
find . -name "file.txt" # Search in current directory
find . -name "*.log" # Search all .log files in current directory
find . -iname "readme.md" # Search insensitive
find . -type d -name "config" # Search for directories only
find . -type f -name "*.sh" # Search for files only
find . -size +10M # Search with size
find . -size -100k
find . -mtime +7 # Search with modify time (Days)
find . -mtime -3
```

### Using -exec in Find:
> `-exec` is using for execute a command on the output of the `find`.

```bash
find . -type f -name "*.log" -exec rm {} \; # Find all .log files & Remove them.
find . -type f -name "*.sh" -exec chmod +x {} \; # Find all .sh files & Change their permission.
```

### Using xargs in Find:
> `-exec` execute command for each file separately, bit `xargs` will execute command for all files together.

```bash
find . -type f -name "*.log" | xargs rm # Find all .log files & remove them.
find . -type f -name "*.log" -print0 | xargs -0 rm # Using -print0 & -0 for special characters (# $ & , space)
find . -type f -name "*.txt" | xargs wc -l # Find all .txt files & count all their lines.

```
> If files have space or special characters, `xargs` may interrupt.

### Locate:
> `Locate` is faster than `find`, because it uses database. But database may have old data and need to update.

```bash
apt install mlocate # Installing locate
updatedb # Update database
locate myconfig.conf # Search a file with exact name.
locate sshd_config # Search with part of a file name.
locate nginx.conf | grep "^/etc" # Filter the search with grep.
locate bin/nano # Find executive binary files.
```

## Files & Directory permissions

### Permissions:
```bash
ls -l # Show file & directory permissions
-rw-r--r-- 1 user group 1234 Jul 13 14:00 example.txt

sudo chown user:group filename # Change file's owner

chmod u+x filename     # Set execution permision for User Owner
chmod g-w filename     # Remove Write permission for Group
chmod o=r filename     # Set just Read-only permission for Others
```

#### Permissions in Numeric mode:

* `rwx` : 7
* `rw-` : 6
* `r-x` : 5
* `r--` : 4
* `-wx` : 3
* `-w-` : 2
* `--r` : 1
* `---` : 0

```bash
# Examples:
chmod 755 script1.sh  # rwxr-xr-x
chmod 644 notes.txt    # rw-r--r--
```
```bash
chmod -R 755 dir1/ # Set permission recursive.
```

### Change Permissions:

```bash
# Change permissions:
chmod [user][operator][permissions] [file]
chmod u+x run.sh
chmod go-w notes.txt
chmod a+r file.txt
chmod u=rw,go=r data.txt
```
```bash
# Change permissions in numeric mode:
chmod [permission] [filename]
chmod 755 script.sh    # rwx r-x r-x
chmod 700 secret.txt   # rwx --- ---
chmod 644 notes.txt    # rw- r-- r--
chmod 600 config.conf  # rw- --- ---
```

### Change Owner:

```bash
chown [user] [file]
chown asghar test.txt
chown asghar:admins test.txt # Change Owner & Group
chgrp admins test.txt # Change Group
chown user1 file1 file2 file3 # Change Owner in Multi-file
chown -R asghar:admins /var/www/ # Change Owner & Group Recursive
```

### Default permission & Umask:

> `umask` will specify the default permissions for new Files & Directories.
* `File` : 666 (rw-rw-rw-)
* `Dir`  : 777 (rwxrwxrwx)

```bash
umask # Display current umask
# Default umask is 0022 
```
* `File` : 666 - `022` = 644 → rw-r--r--
* `Dir`  : 777 - `022` = 755 → rwxr-xr-x

```bash
umask 0077 # Change umask Temporary
```
```bash
# Change umask permanent:
# Edit .bashrc
nano ~/.bashrc
# Add umask:
umask 0077
# Save & run this:
source ~/.bashrc
```

### SUID, SGID, Sticky Bit:

#### Set User ID:

> If a file has `SUID`, it will run with the permission of the `Owner` of the file, not the user who run the file.

```bash
# Example:
ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root ...
```
```bash
chmod u+s file # Set SUID 
```

#### Set Group ID:

> On executive file, it will run with the permission of the Group Owner of the file.
```bash
chmod g+s myscript.sh
```

> All files & directories created under a directory with `SGID` permission, will get the membership of the Group Owner of the directory.

```bash
mkdir /shared
chown root:admins /shared
chmod g+s /shared # All new created files' Group Owner will be admins Group.
```

#### Sticky Bit:

> Only for Directories.
> Only the Owner of the files can delete them, even if others have the read/write permissions.

```bash
# Example:
ls -ld /tmp
drwxrwxrwt 10 root root ...
```
```bash
chmod +t /some/dir # Set Sticky bit on a directory
```

* `s` : SUID / SGID enable with execution
* `S` : SUID / SGID enable without execution
* `t` : Sticky bit enable with execution
* `T` : Sticky bit enable without execution













