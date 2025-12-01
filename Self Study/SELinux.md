# SELinux:

```sh
sestatus
# Output:
SELinux status:                 enabled
Current mode:                   enforcing
Policy from config file:        targeted

# Config file:
/etc/selinux/config
```

```sh
# Enable SELinux:
vim /etc/selinux/config
# Change "disable" to "enforcing" or "permissive"
SELINUX=enforcing
SELINUXTYPE=targeted

reboot # Reboot to apply
```

### SELinux Sections:
1. Contexts
2. Policies
3. Booleans

#### Contexts:
> Each `file`, `directory`, `process` and `port` has a context.

```sh
# File:
ls -Z /var/www/html

# Process:
ps -eZ | grep nginx

# Port:
semanage port -l
```

#### Policies:
* `Targeted` : Default, only important services have been limited.
* `MLS` : Multi=layer security, complicated & heavy.

#### Booleans:
> `Booleans` are keys to On/Off SELinux behavior.

```sh
getsebool -a # Display booleans
# Allow Ngins to have access to Network:
setsebool -P httpd_can_network_connect on
# Allow Apache to work on ports 8080 (Apache by default limited to 80 & 443):
semanage port -a -t http_port_t -p tcp 8080
```






