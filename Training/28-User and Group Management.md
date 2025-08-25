# 28-User and Group Management

**useradd:**
```bash
useradd reza
useradd -m reza
useradd -m -d /home/user1 user1
useradd -m -d /home/user2 -c "Admin User" user2
useradd -m -d /home/user3 -c "Admin User" -s /bin/bash user3
```
* `-d` => home directory of the new account
* `-m` => create the user's home directory
* `-s` => login shell of the new account
* `-G` => add to Additional Groups
* `-c` => comment, most of the time user's actual name

> In most distributions  useradd creates home directory for the new user but we can make sure using -m switch.

**passwd:**
```bash
passwd UserName 
```
**/etc/skel:**

> The home directory skeleton.

When you create a new user and a new home directory is created, the directory is populated with several files and subdirectories that, by default, are copied from /etc/skel.

```bash
root@ubuntu16-1:~# ls -a /etc/skel/
.  ..  .bash_logout  .bashrc  examples.desktop  .profile
```
**usermod:**
```bash
usermod
usermod -s /bin/bash reza
usermod -c "NOC User" reza
usermod -m -d /opt/reza reza
usermod -g NewPrimaryGroup UserName
usermod -G AdditionalGroup UserName
usermod -aG AdditionalGroup UserName
usermod -L reza
usermod -U reza
```
* `-g` => Change Primary Group
* `-G` => Add Additional Group (Just one additional group)
* `-aG` => Add multiple additional group
* `-L` => Lock user account
* `-U` => Unlock user account

**userdel:** 
```bash
userdel
userdel -f -r reza
```
* `-f` => Force delete
* `-r` => Remove home directory

**groupadd:**
```bash
groupadd
groupadd GroupName
groupadd -g 1100 group2 # Change or add new primary group with new GID.
```
**groupmod:**
```bash
groupmod
groupmod -n NewGroup group1 # Rename the group (with same GID)
groupmod -g 1200 NewGroup # Change the group GID.
```
**groupdel:**
```bash
groupdel GroupName
```
**/etc/group:**
> `/etc/group` is the _group_ file containing basic information about groups and which users belong to them. It contains one line for each group in the system.

```bash
root@ubuntu16-1:~# tail /etc/group
milad:x:1000:
sambashare:x:128:milad
user1:x:1001:
mysql:x:129:
user2:x:1002:
postfix:x:130:
postdrop:x:131:
mysecuregroup:x:1003:
```

1. **group_name**: It is the name of group. If you run "ls -l" command, you will see this name printed in the group field. 
2. **Password**: Generally password is not used, hence it is empty/blank. It can store encrypted password. This is useful to implement privileged groups. 
3. **Group ID (GID)**: Each user must be assigned a group ID. You can see this number in your `/etc/passwd` file. 
4. **Group List**: It is a list of user names of users who are members of the group. The user names, must be separated by commas.

**/etc/passwd:**

> `/etc/passwd` is the _password_ file containing basic information about users.
```bash
root@server:~# tail /etc/passwd
sshd:x:121:65534::/var/run/sshd:/usr/sbin/nologin
mysql:x:122:129:MySQL Server,,,:/nonexistent:/bin/false
milad:x:1000:1000:Milad Norouzi:/home/milad:/bin/bash
user1:x:1001:1001::/home/user1:
user2:x:1002:1002::/home/user2:
```
It has one line for each user in the system. the format of it is :

1. **Username**:  should be between 1 and 32 characters 
2. **Password**_(will be discussed)_
3. **User ID (UID)**: Each user must be assigned a user ID (UID). UID 0 (zero) is reserved for root and UIDs 1-99 are reserved for other predefined accounts. Further UID 100-999 are reserved by system for administrative and system accounts/groups. 
4. **Group ID (GID)**: The primary group ID (stored in /etc/group file) 
5. **The comment field**. It allow you to add extra information about the users such as user’s full name, phone number etc. This field use by finger command. 
6. **Home directory**
7. **Command/shell**: The absolute path of a command or shell (/bin/bash). Typically, this is a shell. It does not have to be a shell.

> There are some users with `/sbin/nologin` shell, They are actually system accounts that run a service and no one can interactively login using them. Some times it has been set to `/bin/false`. 
Every user should have read access to `/etc/passwd`  :

```bash
root@ubuntu16-1:~# ls -l /etc/passwd
-rw-r--r-- 1 root root 2469 Feb 12 02:53 /etc/passwd
```

> In old days there was a place that  all users information even the user's password, and it is not so hard thick about security issue that it caused. To solve the problem `/etc/shadow` was invented.  An x character indicates that encrypted password is stored in `/etc/shadow` file

**/etc/shadow:**

> The `/etc/shadow` file contains encrypted passwords, along with password- and account-expiration information.

```bash
root@ubuntu16-1:~# ls -l /etc/shadow
-rw-r----- 1 root shadow 1609 Feb 12 02:53 /etc/shadow
```
```bash
root@ubuntu16-1:~# tail /etc/shadow
pulse:*:17379:0:99999:7:::
rtkit:*:17379:0:99999:7:::
saned:*:17379:0:99999:7:::
usbmux:*:17379:0:99999:7:::
milad:$1$jYgAdos4$Je8la0839ZRVgazhnBpDv1:17496:0:99999:7:::
user1:$6$c9PN.175$.t.CG0E0Gtr/trq4pqquSe1BemMjB6Zc3E0ExUOVufuTkPNe3BSRv3DyUuXFHPiAbEujzuSMCeMsCbpg8cV2j.:17749:0:99999:7:::
sshd:*:17749:0:99999:7:::
mysql:!:17867:0:99999:7:::
user2:$6$kN2DNYrP$XmM/3ONRnrTCuTTBxCwVBlVW9E4tVRc02JbRHPhwj128Q6aUIcUq4gxw2r74gopOs2J0HqNxuiBiqgAlkmuwV1:18290:0:99999:7:::
postfix:*:18300:0:99999:7:::
```
> **Note:** `!!` means user can not log in with any passwords. Most of service accounts are like this.
Passwords can be encrypted with one of several encryption algorithms. Older systems used DES or MD5, but modern systems typically use Blowfish, SHA-256, or SHA-512, or possibly MD5. Regardless of encryption algorithm, passwords are _salted_ so that two otherwise identical passwords do not generate the same encrypted value.

1. **Username** : It is your login name. 
2. **Password** : It is your encrypted password. The password should be minimum 8-12 characters long including special characters, digits, lower case alphabetic and more. Usually password format is set to `$id$salt$hashed`, The $id is the algorithm used On GNU/Linux as follows: $1$ is MD5 $2a$ is Blowfish $2y$ is Blowfish $5$ is SHA-256 $6$ is SHA-512.
3. **Last password change (lastchanged)** : Days since Jan 1, 1970 that password was last changed 
4. **Minimum**: The minimum number of days required between password changes i.e. the number of days left before the user is allowed to change his/her password
5. **Maximum**: The maximum number of days the password is valid (after that user is forced to change his/her password)
6.  **Warn** : The number of days before password is to expire that user is warned that his/her password must be changed 
7. **Inactive**: The number of days after password expires that account is disabled 
8. **Expire** : days since Jan 1, 1970 that account is disabled i.e. an absolute date specifying when the login may no longer be used.

> The last 6 fields provides password aging and account lockout features. You need to use the `chage` command to setup password aging.

**chage:**
```bash
chage
chage -l reza # Show aging information of a user account
chage -d 0 reza # Force user to change his password.
```




