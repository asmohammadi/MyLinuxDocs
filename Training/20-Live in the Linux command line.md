# 20-Live in the Linux command line

* `ls`
* `touch`
* `stat`
* `TimeStamp`
* `mkdir`
* `cp`
* `mv`
* `rm`

### ls:
```bash
ls
ls -l # Long term(Show modified time)
ls -a
ls -la
ls -lash
ls -1 # Display just names
```
### touch:
```bash
touch FileName
touch -t YYMMDDHHMM FileName # Create file and add time stamp on it.
touch -t 202510281645 file1 # 2025/10/28 16:45
```
```bash
touch file{1..10} # Create file1 file2 ... file10
```
### stat:
```bash
stat File # Show status of a file.
```
```bash
root@server:~# stat file1
  File: file1
  Size: 0           Blocks: 0          IO Block: 4096   regular empty file
Device: 801h/2049d    Inode: 1200795     Links: 1
Access: (0644/-rw-rw-r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2019-09-08 02:34:44.962514623 -0700
Modify: 2018-07-01 23:15:30.140815060 -0700
Change: 2018-07-01 23:15:30.144817112 -0700
Birth:  2018-07-01 23:15:30.144817112 -0700
```
**Time Stamp:**
> A file in Linux has three timestamps:
* `atime` `(access time)` : The last time the file was accessed/opened by some command or application such as cat, vim or grep.
* `mtime` `(modify time)` : The last time the file’s content was modified.
* `ctime` `(change time)` : The last time the file’s attribute or content was changed. The attribute includes file permissions, file ownership or file location.

### mkdir:
```bash
mkdir 
mkdir -p dir1/dir2/dir3 # Create directories recursive with their Parent.
tree # Show directories in tree mode.
mkdir -m777 dir1 # Create directory with specific permission.
```
### cp:
```bash
cp
cp file1 /dir1/ # Copy a file to a directory.
cp /dir/file1 . # Copy a file from another directory to here.
cp file1 file2 dir1/ # Copy multiple files to a directory.
cp -r dir1 /newdir1/ # Copy a directory to another directory recursively.
```
### mv:
```bash
mv
mv file1 dir1/
mv dir1/ /dir2/
mv file1 file2 # Rename the file.
```
### rm:
```bash
rm
rm -f # Force remove
rm -d dir/ # Remove just empty directories.
rm -r dir/ # Remove directories recursively.
rm -fr /* # Remove all files in system.
rmdir dir/ # Remove just empty directory.
rmdir dir\{1.10\}/ # Remove dir1, ..., dir10
```





