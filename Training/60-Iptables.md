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








