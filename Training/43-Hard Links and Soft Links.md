# 43-Hard Links and Soft Links

### Hard Links vs Soft Links

**Hard Links:**
* Have same inodes number
* Can’t cross the file system boundaries
* Can’t link directories
* Links have actual file contents
* If the original file is removed, the link will still show you the contents of the file
* Permissions will be updated if we change the permissions of source file

**Soft Links:**
* Have different inodes numbers.
* Can cross the file system 
* Allows you to link between directories
* Contains the path for original file and not the contents
* Removing soft link doesn't affect anything but when the original file is removed, the link becomes a 'dangling' link that points to nonexistent file
* Permissions will not be updated   

### Create Links:

**Hard Link:**
```bash
ln Original_Filename Link_Name 
ln File2 HardLink2

root@ubuntu:~/# ls -1i
2228289 File1
2228289 HardLink2
```

**Soft link:**
```bash
ln -s Original_Filename Link_Name
ln File3 SoftLink3

root@ubuntu:~/# ls -1
-rw-r--r-- 2 root root    0 Jan 29 08:14 file2
-rw-r--r-- 1 root root    0 Jan 29 09:05 file3
-rw-r--r-- 2 root root    0 Jan 29 08:14 HardLink
lrwxrwxrwx 1 root root    5 Jan 29 09:06 SoftLink -> file3

root@ubuntu:~/# ls -1i
2228291 file3
2228289 SoftLink3

###creating soft link to a directory
root@ubuntu16-1:~/sandbox# ln -s dir/ soft2dir

root@ubuntu16-1:~/sandbox# ls -l | grep soft2dir
lrwxrwxrwx 1 root root   4 Feb  2 00:04 soft2dir -> dir/
```

**Unlink:**
```bash
unlink SoftLink3 # Remove Soft Link
```



