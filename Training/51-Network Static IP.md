# 51-Network Static IP

### Network files Path:
* Debian/Ubuntu : `/etc/network/interfaces` / `/etc/network/interfaces.d/`
* RedHat/CentOs : `/etc/sysconfig/network`  / `/etc/sysconfig/network-scripts`

### Ubuntu Static IP Configuration:

> Where to set Static configuration:
* Ubuntu : `/etc/netplan`
* Debian : `/etc/network/interfaces`
* CentOs : `/etc/sysconfig/network-scripts/`

**Netplan/50-cloud-init.yaml:**
```bash
50-cloud-init.yaml

# This file is generated from information provided by the datasource.  Changes
# to it will not persist across an instance reboot.  To disable cloud-init's
# network configuration capabilities, write a file
# /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
# network: {config: disabled}
network:
    ethernets:
        ens36:
            dhcp4: true
        ens37:
            dhcp4: no
                addresses:
                    - 192.168.64.100/24
                # gateway4: 192.168.64.1
                nameservers:
                    addresses: [8.8.8.8, 1.1.1.1]
        ens38:
            dhcp4: no
                addresses:
                    - 192.168.64.200/24
                route:
                    - to: 172.16.00/24
                    - via: 192.168.1.1
                    - to: default
                    - via: 192.168.1.1
                nameservers:
                    addresses: [8.8.8.8, 1.1.1.1]
    version: 2
~
```
> `References:` https://netplan.readthedocs.io 

**Netplan:**
```bash
netplan try # Checking netplan Yaml configuration and set configuration.
netplan apply # Set configuration without checking.
```

### Debian Static IP Configuration:

**/etc/network/interfaces:**
```bash
# The Loopback network interface
auto lo
iface lo

# The primary network interface
allow-hotplug eth0
iface eth0 inet dhcp

# This is an autoconfigured IPv6 interface
iface eth0 inet6 auto

auto eth1
iface eth1 inet static
        address 192.168.64.100/24
        network 192.168.64.0
        broadcast 192.168.64.255
#         gateway 192.168.64.1
        dns-nameservers 8.8.8.8
```
```bash
systemctl restart networking.service # To set configuration.
```

### CentOs Static IP Configuration:

**/etc/sysconfig/network-scripts/**

```bash
root@ubuntu:~# vim ifcfg-ens36

# static IP address on CentOS 7 or RHEL 7#
TYPE=Ethernet
BOOTPROTO=none
IPADDR=192.168.2.203
PREFIX=24
GATEWAY=192.168.2.254
DNS1=192.168.2.254
DNS2=8.8.8.8
DNS3=8.8.4.4
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=no
NAME=eth0
DEVICE=eth0
ONBOOT=yes
```
```bash
systemctl restart network # To set configuration.
```


