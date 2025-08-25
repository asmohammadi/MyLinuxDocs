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
iptables -t filter -P INPUT drop
```
```sh
iptables -L -t filter # List all rules in Filter table
iptables -L -t nat
iptables -L -t mangle
iptables -nvL -t filter # Numeric & Verbose
iptables -nvL -t filter --line-number # Display rule numbers
```



