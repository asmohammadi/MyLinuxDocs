# 55-SSH (Server side)

### Edit SSH Server Configurations:
```bash
# Edit sshd_config:
vim /etc/ssh/sshd_config
# Change SSH Port Number:
Port 22 => Port 2222
# Secure SSH Connection:
AddressFamily any # Choose v4 or v6 IP Addresses
ListenAddress 0.0.0.0 # Listen from which Network Card or IP Address
# Authentication:
PermitRootLogin prohibit-password => No # Root cannot login with SSH.
MaxAuthTries 6 # Maximum wrong try
MaxSessions 10 => MaxSessions 4 # Maximum parallel sessions (connections)
# Public Key Authentication:
PublicKeyAuthentication yes # By default is Yes.
# Disable password-base SSH connection:
PasswordAuthentication yes => No
```
### Second Path of SSH Configurations (Ubuntu 22.04 & later):
```bash
# /etc/ssh/sshd_config.d/50-cloud-init.conf
# Disable password-base SSH connection:
PasswordAuthentication yes => No
```

### Apply SSH Configuration Changes:
```bash
systemctl daemon-reload && systemctl restart ssh # In Ubuntu 22.04 & later
systemctl restart sshd # In other OS (Debian, RedHat, CentOs)
```









