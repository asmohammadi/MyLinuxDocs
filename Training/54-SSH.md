# 54-SSH

### Install SSH on Server:
```bash
apt install openssh-server
# Install openssh-client
# Install openssh-server
# Install openssh-sftp-server
```
```bash
# Checking SSH service:
systemctl status ssh.service
systemctl status sshd.service # Before Ubuntu22.04, RedHat, Debian
```
```bash
root@server:~# ls -1 /etc/ssh/
moduli
ssh_config
ssh_config.d
sshd_config
sshd_config.d
ssh_host_ecdsa_key
ssh_host_ecdsa_key.pub
ssh_host_ed25519_key
ssh_host_ed25519_key.pub
ssh_host_rsa_key
ssh_host_rsa_key.pub
ssh_import_id
```

```bash
# /home/user/.ssh/ on Client:
user@client:~#ls -1 .ssh/
authorized_keys # Uses for Server-side as Public keys holder.
known_hosts # Servers which client has been connected to.
known_hosts.old
```

### Generating Key:

**ssh-keygen:**
> `ssh-keygen` creates a key pair for public key authentication.

```powershell
# Generate Keys on Windows Client:
ssh-keygen -t rsa -b 4096 -C "user1@ubuntu-client"
Default Path: C:\Users\user1\.ssh\id_rsa # For changing the name of file put the Path & Name.
Enter Passphrase: # Enter for No Passphrase.
```
* `-t` : Type of Algorithm (dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa)
* `-b` : Bits
* `-f` : File Name
* `-C` : Comment


```bash
# Generate Keys on Linux Client:
user1@client:~$ ssh-keygen 

Generating public/private rsa key pair.
Enter file in which to save the key (/home/user1/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/user1/.ssh/id_rsa.
Your public key has been saved in /home/user1/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:rer76yQU+8Mmrg33xCA51RtnpTUVHT1cVMX7kB2+aUI user1@ubuntu16-2
The key's randomart image is:
+---[RSA 2048]----+
|            +.+*@|
|       .   + . ++|
|      o o +   .o+|
|     o o *   Eoo.|
|    + + S . .  .+|
|     + = .   . +.|
|    . + X     o  |
|     = O .       |
|    .o*+=.       |
+----[SHA256]-----+
```
```bash
user1@client:~$ tree .ssh/
.ssh
├── id_rsa
├── id_rsa.pub
└── known_hosts

0 directories, 3 files
```
### Copy Public Key to Server:

**ssh-copy-id:**
> `ssh-copy-id` configures a public key as authorized on a server.

```bash
ssh-copy-id -i .ssh/id-rsa.pub root@Server_IP
```
* `-i` : Identity File
* `-t` : Target Path
* `-f` : Force
* `-s` : Use Sftp






