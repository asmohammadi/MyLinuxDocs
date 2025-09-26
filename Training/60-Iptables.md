# 60-Iptables

**Iptables:**
* `UFW` : Debian / Ubuntu
* `Firewalld` : RedHat /CentOS

`Kernel` -> `NetFilter` => `Nftable` -> `Iptables` => `UFW / Firewalld`

**Tables:**
* Filter
* NAT
* Mangle
* Row

**Chains:**
* PreRouting
* Input
* Output
* Forward
* PostRouting

**Tables & Chains:**
* `Filter` : Input, Output, Forward
* `NAT`    : PreRouting, Output, PostRouting
* `Mangle` : PreRouting, Input, Output, Forward, PostRouting
* `Row`    : PreRouting, Output

## Actions:
* ACCEPT
* DROP
* REJECT
* LOG
* MASQUERADE

## Iptables Command Structure:
```sh
iptables Option Chain -t Table [-i/-o Interface] [-s/-d Address] -p UDP/TCP/ICMP --sport/--dport PortNumber -j Action
iptables -A input -t filter [-i eth0] [-s 192.168.10.1] -p tcp --sport 22 -j ACCEPT
# Allow traffic from Eth0 from 192.168.10.1 on port 22 and Accept it.
```
* `-A` : Append to Chain
* `-D` : Delete
* `-I` : Insert (Default RuleNum : First)
* `-C` : Check for the existence of a rule
* `-R` : Replace rule's RuleNumber
* `-L` : List rules
* `-S` : Print rules
* `-F` : (Flush) Delete all rules
* `-t` : Table (Default : Filter)
* `-i/-o` : Input/Output of Interface
* `-s/-d` : Source/Destination Address
* `-p` : Protocol Type (TCP/UDP/ICMP)
* `--sport/--dport` : Source Port/Destination Port
* `-j` : Action

```sh
Change Filter (INPUT) : ACCEPT --> DROP
iptables -P drop INPUT # Change the Filter Table default Policy from ACCEPT to DROP
iptables -t filter -P INPUT DROP
```
```sh
iptables -L -t filter # List all rules in Filter table
iptables -L -t nat
iptables -L -t mangle
iptables -nvL -t filter # Numeric & Verbose
iptables -nvL -t filter --line-number # Display rule numbers
```

```sh
iptables -t filter -A INPUT -p ICMP -s 192.168.178.21 -j DROP
iptables -t filter -D INPUT 1 # Delete rule number one
iptables -t filter -A INPUT 2 -p ICMP -s 192.168.178.21 -j ACCEPT # Add rule with RuleNumber 2, Add between the rules.
iptables -t filter -I INPUT -p TCP -s 192.168.178.21 --dport 80 -j DROP
```

```sh
iptables -t filter -I INPUT -p TCP -s 192.168.178.21 --dport 80 -j DROP
iptables -t filter -I INPUT -p TCP -s 192.168.178.21 --dport 3306 -j DROP
# or:
iptables -t filter -I INPUT -p TCP -s 192.168.178.21 -m multiport --dports 80,3306 -j DROP # Add Multiport 
```

```sh
# Specific Interface:
iptables -t filter -A INPUT -i ens33 -j LOG --log-prefix "IPTABLES dROPPED:" # Just create log
```

```sh
# Redirect:
iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
iptables -nvL -t nat
```

### Packet States:
* `New`
* `Related`
* `Stablished`
* `Valid`

```sh
# Everything Drop, Except ACCEPT rules for SSH:
iptables -t filter -I INPUT -p TCP -s 192.168.178.21 --dport 22 -j ACCEPT # Receive
iptables -t filter -I OUTPUT -p TCP --sport 22 -D 192.168.178.21 -j ACCEPT # Send
iptables -t filter -A INPUT -j DROP
iptables -t filter -A OUTPUT -j DROP
```

```sh
# ACCEPT Established & Related state packets:
iptables -t filter -I OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```

### Sample Scenario:
* Accept Loopback connections (For local services communication)
* Accept SSH,HTTP,Ping to Server
* Accept UDP DNS from Server
* Accept TCP DNS,HTTP,HTTPS from Server
* Accept Receive/Answer DNS,HTTP,HTTPS to Server
* DROP everything else

```sh
iptables -t filter -A INPUT -i lo -j ACCEPT # Loopback
iptables -t filter -A OUTPUT -o lo -j ACCEPT # Loopback

iptables -t filter -A INPUT -p tcp --dport 22 -j ACCEPT # Receive SSH
iptables -t filter -I INPUT -p tcp --dport 80 -j ACCEPT # Receive HTTP
iptables -t filter -I INPUT -p ICMP -j ACCEPT # Receive Ping
iptables -t filter -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT # For SSH,HTTP,Ping Answer

iptables -t filter -A OUTPUT -p udp --dport 53 -j ACCEPT # Send UDP DNS, APT Install/Update/Upgrade
iptables -t filter -A OUTPUT -p tcp -m multiport --dports 53,80,443 -j ACCEPT # Send TCP DNS, HTTP, HTTPS
iptables -t filter -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT # For DNS,HTTP,HTTPS Answer

iptables -t filter -A INPUT -j DROP # Drop Everything Else
iptables -t filter -A OUTPUT -j DROP # Drop Everything Else
```

### User-defined Chain:
* Creating Chain, instead of creating Rules.
* Adding custom chains to the default chains.
```sh
# Create User-defined Chains:
iptables -t filter -N SSH-IN
iptables -t filter -N SSH-OUT
# Create Rules in User-defined Chains:
iptables -t filter -A SSH-IN -p tcp -s 192.168.0.0/24 --dport 22 -j ACCEPT
iptables -t filter -A SSH-OUT -p tcp -d 192.168.0.0/24 --sport 22 -j ACCEPT
# Inject User-defined Chains to default chains:
iptables -t filter -I INPUT -j SSH-IN
iptables -t filter -I OUTPUT -j SSH-OUT
```

### DNAT (IP Forwarding):
> `Forwarding` means make the linux to be a `Router` to forward the packets.

**Temporary Configuration:**
```sh
cat /proc/sys/net/ipv4/ip_forward # By default 0 (disable)
echo 1 > /proc/sys/net/ipv4/ip_forward # Enable Forwarding
```

**Permanent Configuration:**
```sh
vim /etc/sysctl.conf
net.ipv4.ip_forward=1
sysctl -p # Apply changes
```

```sh
# Destination NAT Rule:
iptables -t nat -A PREROUTING -p tcp --dport 80 -d 192.168.178.95 -j DNAT --to-destination 192.168.178.101:80 
iptables -t nat -A POSTROUTING -j MASQUERADE # For return
```

### SNAT (Source Nat):
* Set IP & Gateway on Client (Gateway is Router)
* Set IP & Gateway on Router Server (Gateway is Firewall outside)
* Enable IP Forward on Router Server
* 

```sh
# On client:
vim /etc/netplan/50-cloud-init.yaml # Add IP & Gateway
```
```sh
# On Router Server:
vim /etc/netplan/50-cloud-init.yaml # Add IP & Gateway
vim /etc/sysctl.conf # Enable IP Forward
sysctl -p # Apply changes
```
```sh
# Create Rules:
iptables -t nat -A POSTROUTING -o enp0ps3 -j MASQUERADE # Source NAT
iptables -t filter -A FORWARD -i enp0s8 -j ACCEPT
```

### Save Iptables Configuration:
* `Temporary` : Save to a file (Not recommend)
* `Permanent` : Using Cron (Not recommend)
* `Permanent` : Using `iptables-persistent` Package
```sh
# Temporary (Not recommend):
iptables-save > /path/file.txt # Save configuration as a text file
iptables-restore < /path/file.txt # Restore configuration from a text file
```
```sh
# Permanent with Cron (Not recommend):
vim /etc/crontab # Add file.txt to Cron
@reboot root iptables-restore < /path/file.txt
```
```sh
# Permanent (Recommended):
apt install iptables-persistent
/etc/iptables/rules.v4 # Path of saved iptables configuration (Will restore at reboot)
iptables-save > /etc/iptables/rules.v4 # Will restore after reboot
# Apply changes without reboot:
iptables-apply -t 10 /etc/iptables/rules.v4 # Apply change temporary, but wait 10 seconds to get confirmation, if no answer it will Rollback changes.
```























