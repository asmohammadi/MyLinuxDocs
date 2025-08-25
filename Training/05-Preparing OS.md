# 05-Preparing OS

### Network Commands:
#### Show IP Addresses

```Bash
ip -br a
```
#### Make a User Sudoer:

```Bash
# Create a file in this path:
nano /etc/sudoers.d/user1
```
```sh
# Add this to the file:
user1 ALL=(ALL) NOPASSWD:ALL
```
#### Disable IPv6:
```bash
sysctl -w net.ipv6.conf.all.disable_ipv6=1
sysctl -w net.ipv6.conf.default.disable_ipv6=1
```



