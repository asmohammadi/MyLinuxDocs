# 41-Managing file permissions

**chmod:**
```bash
chmod u+x file1 # Add Execute permission to the User.
chmod u-wx file1 # Remove Write & Execute permission from the User.
chmod g+wx file1 # Add Write & Execute permission to the Group.
chmod g-r file1 # Remove Read permission from the Group.
chmod o+rwx file1 # Add Read, Write & Execute permission to the Others.
chmod u-rwx,g-rwx file1 # Remove Read, Write & Execute permission from User & Group.
chmod ug=rx,o=x file1 # Add Read & Execute to User & Group and Add Execute to the Others.
chmod a=rwx file1 # Add Read, Write & Execute permission to All (User, Group & Others).
chmod 537 file1 # User=rx , Group=wx , Others=rwx
chmod 777 Dir1/ # Add rwx permission on a directory. (Not subdirectories)
chmod -R 777 Dir1/ # Add rwx permission on a Directory & its Subdirectories & Files.
```

**chown:**
```bash
chown user1:Group1 file2 # Change the User Owner & Group Owner of a File.
chown milad:milad dir2/
chown -R milad:milad dir2/ # Change the User Owner & Group Owner on a Directory & its Subdirectories & Files.
```

**chgrp:**
```bash
chgrp root dir1/ # Change the Group
```

**SUID:**
> The Linux permissions model has two special access modes called `suid` (set user id) and `sgid` (set group id). When an executable program has the `suid` access modes set, it will run as if it had been started by the file’s owner, rather than by the user who really started it. Similarly, with the `sgid` access modes set, the program will run as if the initiating user belonged to the file’s group rather than to his own group.
> `SUID` will set on files.

**SGID:**

> When a directory has the `sgid` mode enabled, any files or directories created in it will inherit the group ID of the directory. This is particularly useful for directory trees that are used by a group of people working on the same project.
> `SGID` will set on Directories.

**Sticky Bit:**
> We have just seen how anyone with write permission to a directory can delete files in it. This might be acceptable for a group project, but is not desirable for globally shared file space such as the /tmp directory. Fortunately, there is a solution.  That  is called the `sticky bit`.

> If set `sticky bit` for a directory, it permits only the owning user or the superuser (root) to delete or unlink a file. 

| access mode    | **on file**                             | **on directory**                             |
| -------------- | --------------------------------------- | -------------------------------------------- |
| **SUID**       | executes with permissions of file owner | nothing                                      |
| **SGID**       | executes with the permissions of group  | new files have group membership of directory |
| **Sticky Bit** | nothing                                 | only owner can delete files                  |

| Access Mode   | octal |
| ------------- | ----- |
| **SUID**      | 4000  |
| **SGID**      | 2000  |
| **StickyBit** | 1000  |

* `s` : SUID with Execute permission
* `s` : SGID with Execute permission
* `t` : Sticky Bit with Execute permission
* `S` : File or Directory has no Execute permission (For User & Group)
* `T` : File or Directory has no Execute permission (For Others)

> If the file or directory is already executable **`s`** and **`t`** would be displayed after setting access modes. 

> But if the file or directory hasn't been executable before setting access mode, **`S`** and **`T`** would be appear.

**Umask:**
> When a new file is created, the creation process specifies the permissions that the new file should have. Often, the mode requested is 0666, which makes the file readable and writable by anyone (but not executable). Directories usually default to 0777. However, this permissive creation is affected by a _umask_ value, which specifies what permissions a user does **not** want to grant automatically to newly created files or directories. The system uses the umask value to reduce the originally requested permissions.
```bash
root@ubuntu:~# umask
0022
```

> Usually umask  is set system wide (it could be set per user) and we can find its configuration in one of these places (based on your linux distribution): 

* /etc/profile (usually)
* /etc/bashrc (usually)
* /etc/logindefs (ubuntu)



