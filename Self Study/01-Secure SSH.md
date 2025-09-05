# Secure SSH

### Create Certificate Keys (General & Public) on Client:

**On Windows Client:**
```powershell
ssh-keygen -t rsa -b 4096 -C "root@ubuntu24.04"
# or
ssh-keygen -t ed25519 -C "email@example.com" # More safe algorithm

Default Path: C:\Users\UserName\.ssh\id_rsa # For changing the name of file put the Path & Name.
Enter Passphrase: # Enter for No Passphrase.
```
* `-t` : Type of Algorithm
* `-b` : Bits
* `-f` : File Name
* `-C` : Comment

**On Linux Client:**
```sh
ssh-keygen -t rsa -b 4096 -C "email@example.com"
# or
# Private Key:
openssl genpkey -algorithm RSA -out id_rsa -aes256 -pkeyopt rsa_keygen_bits:4096
# Extract Public Key:
openssl rsa -pubout -in id_rsa -out id_rsa.pub
# or
# Private Key:
openssl genpkey -algorithm ED25519 -out id_ed25519.pem
# Extract Public Key:
openssl pkey -in id_ed25519.pem -pubout -out id_ed25519.pub

# Convert OpenSSL PEM to authorized_keys for using in SSH:
ssh-keygen -y -f id_rsa > id_rsa_ssh.pub
ssh-keygen -y -f id_ed25519.pem > id_ed25519_ssh.pub
```

```powershell
PS C:\Users\Asghar> ssh-keygen -t rsa -b 4096 -C "root@ubuntu24.04"
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\Asghar/.ssh/id_rsa):
Created directory 'C:\Users\Asghar/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\Asghar/.ssh/id_rsa
Your public key has been saved in C:\Users\Asghar/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:ZYfU3Arr/MIFZG/ca+z92UiqaWRkql/U7lH9LuRGf0M root@ubuntu24.04
The key's randomart image is:
+---[RSA 4096]----+
|          .o .   |
|         .+.o .  |
|         o+=.o   |
|         o=o= .. |
|        S*.o.....|
|        ..=...*E.|
|       . +.oo*oo.|
|      .  .+o.+=+*|
|       ...ooo..oB|
+----[SHA256]-----+
```

### Copy Keys to Server:
```bash
# For Linux Clients:
ssh-copy-id
```
```powershell
# For Windows Clients:
1. Open public key & copy the content # On Windows Client
2. Create path & file "~/.ssh/authorized_keys" or "/home/username/.ssh/authorized_keys" # On Linux Server
3. Paste content to the "authorized_keys" and save it.
4. Add permission to Dir & File
    chmod 700 ~/.ssh
    chmod 600 ~/.ssh/authorized_keys
5. Logout
```

### Change SSH Port Number:
```bash
nano /etc/ssh/sshd_config # Edit SSH Configuration
port 22 # Uncomment & Change to port 2222
# Save configuration file & Exit
```
```bash
ufw status # Checking Firewall status
ufw allow 2222/tcp # Open port 2222 in Firewall
systemctl restart ssh # Restart SSH Service
## Do not close the current SSH connection before testing the new port.
ssh -p 2222 root@SSH-Server-IP # Test ssh connection
```

### Limit SSH Users:

```bash
nano /etc/ssh/sshd_config # Edit SSH configuration
# Search for this:
AllowUsers username1 username2 # Allowed Users for SSH
systemctl restart ssh
```

### Install & configuring Fail2Ban:
> `Fail2Ban` is an intrusion prevention software, written in the Python programming language. it is designed to prevent brute-force attacks.

```bash
apt install fail2ban -y # Installing Fail2Ban
cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
nano /etc/fail2ban/jail.local # Edit configuration file
```
```bash
# Changing the SSH Port number in configuration file:
[sshd]
enabled = true
port = 2222
logpath = %(sshd_log)s
maxretry = 5
# Save & Exit
```
```bash
systemctl restart fail2ban
systemctl enable fail2ban
systemctl status fail2ban
fail2ban-client status ssh
```
### Installing Monitoring Tools:

* `htop` : Graphical view of CPU Usage, RAM Usage & Processes.
* `iotop` : Display Disk Usage & I/O of Processes.
* `nmon` : Monitoring Tools for CPU, RAM, Disk, Network, . . .
* `net-tools` : Old Tools like `netstat`
* `nmap` : Network scan & Port scan
* `lsof` : Display open files of processes.

```bash
# Installing Tools:
apt install htop iotop nmon net-tools nmap lsof -y
```










