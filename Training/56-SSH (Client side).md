# 56-SSH (Client side)

### Edit SSH Configuration on Client:
```bash
# /etc/ssh/ssh_config

Include /etc/ssh/ssh_config.d/*.conf

Host *
#   ForwardAgent no
#   ForwardX11 no
#   ForwardX11Trusted yes
#   PasswordAuthentication yes
#   HostbasedAuthentication no
#   GSSAPIAuthentication no
#   GSSAPIDelegateCredentials no
#   GSSAPIKeyExchange no
#   GSSAPITrustDNS no
#   BatchMode no
#   CheckHostIP no
#   AddressFamily any
#   ConnectTimeout 0
#   StrictHostKeyChecking ask
#   IdentityFile ~/.ssh/id_rsa
#   IdentityFile ~/.ssh/id_dsa
#   IdentityFile ~/.ssh/id_ecdsa
#   IdentityFile ~/.ssh/id_ed25519
#   Port 22
#   Ciphers aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc
#   MACs hmac-md5,hmac-sha1,umac-64@openssh.com
#   EscapeChar ~
#   Tunnel no
#   TunnelDevice any:any
#   PermitLocalCommand no
#   VisualHostKey no
#   ProxyCommand ssh -q -W %h:%p gateway.example.com
#   RekeyLimit 1G 1h
#   UserKnownHostsFile ~/.ssh/known_hosts.d/%k
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
```
> It is better to copy the `ssh_config` file and customize it for the user which want to connect with SSH.
> Need to create a `config` file under the `/home/user/.ssh/`.

```bash
# Customized Configuration for each SSH Server:
Host mci-db1
  HostName 192.168.178.93
  User user1
  Port 22
  IdentityFile ~/.ssh/id_rsa
Host mci-web
  HostName 192.168.178.94
  User user1
  Port 22
  IdentityFile ~/.ssh/id_rsa
# or
Host mci-*
  User user1
  Port 22
  IdentityFile ~/.ssh/id_rsa

Host mci-web
  HostName 192.168.178.93
Host mci-db1
  HostName 192.168.178.94
Host mci-db2
  HostName 192.168.178.95
# or
include ~/.ssh/config.d/* # In ~/.ssh/conf File.
# Then put the customized config files to the "~/.ssh/config.d/*" path by name.
```
```bash
ssh mci-db1 # Will connect without asking or showing any data.
```







