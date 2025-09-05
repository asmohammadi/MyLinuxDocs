# User & Group Management.md

### Create New User:
```bash
useradd -m username # Create user with Home directory
```
* `-m` : Make Home Directory

### Set Password:

```bash
passwd username # Set or Change Password for a user
```

### Delete User:
```bash
userdel username
userdel -r username # Delete a user with Home directory and files
```

### Change User & Group:
```bash
usermod -g newgroup username # Change the Group of a User
```

### Add a User to a Group:
```bash
usermod -aG group1,group2 username
usermod -aG sudo,docker asghar
```

### Group Membership:
```bash
groups username # Display the Groups of a User
```

### Sudo:
```bash
sudo visudo # Editor of the Sudoers file (Can check the errors)
# Add full permission to a user:
User ALL=(ALL) ALL # Add this line to Sudoers file
%sudo ALL=(ALL) ALL # Add full permission to sudo Group
usermod -aG sudo username # Add a user to Sudoers Group
```
```bash
# User privilege specification
root    ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL
asghar ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
```
* `ALL=`  : User can run `sudo` from any Host
* `(ALL)` : User can run commands as any User (Can change to any user) 
* `ALL:ALL` : Can run command as any User & Group
* `ALL`   : User can run any command

### Check Logs & JournalCTL:
```bash
journalctl -xe # Display recently logs
journalctl -u ssh.service # Display logs of a specific service
last # Display Last logins
who # Display current logged-in users
w # Display current logged-in users & their current activity
cat /var/log/auth.log | grep sudo # Display sudo logs
```

### Disable a User:
```sh
# Lock user:
usermod -L username
passwd -l username
# But still can use SSH with Key:
# Lock with changing Bash:
usermod -s /usr/sbin/nologin username
usermod -s /bin/false username
# Lock full account:
usermod -L -s /usr/sbin/nologin username
# Expire the user:
usermod -e 1 username # Set expire date to before
## Unlock the User:
usermod -U username
usermod -s /bin/bash username
```





