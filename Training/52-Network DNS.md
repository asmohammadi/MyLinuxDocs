# 52-Network DNS

**dig:**
> `Dig` (Domain Information Groper) is a command-line tool for querying DNS name servers.
> `Dig` will query from `/etc/resolv.conf`.
```bash
dig google.com
dig google.com MX # Show MX records
dig google.com NS # Show Nameserver records
dig google.com TXT # Show TXT records
dig @1.1.1.1 google.com # Ask from 1.1.1.1
dig +short @1.1.1.1 google.com # Show just the answer
dig -x 74.6.231.30 # Resolve the IP to Name (Show PTR record)
dig +trace google.com # Trace
dig +noall +answer yahoo.com 
```
```bash
root@ubuntu:~# dig lpi.org

; <<>> DiG 9.10.3-P4-Ubuntu <<>> lpi.org
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 23520
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;lpi.org.			IN	A

;; ANSWER SECTION:
lpi.org.		599	IN	A	65.39.134.165

;; Query time: 501 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Sat Feb 29 17:16:01 +0330 2020
;; MSG SIZE  rcvd: 52
```

**host:**
> `host` command is a DNS lookup utility, finding the IP address of a domain name. It also performs reverse lookups, finding the domain name associated with an IP address.
```bash
host yahoo.com
host 72.30.35.10
```

```bash
root@ubuntu:~# host yahoo.com

yahoo.com has address 72.30.35.10
yahoo.com has address 98.137.246.7
yahoo.com has address 98.138.219.231
yahoo.com has address 98.138.219.232
yahoo.com has address 98.137.246.8
yahoo.com has address 72.30.35.9
yahoo.com has IPv6 address 2001:4998:c:1023::4
yahoo.com has IPv6 address 2001:4998:58:1836::10
yahoo.com has IPv6 address 2001:4998:44:41d::4
yahoo.com has IPv6 address 2001:4998:58:1836::11
yahoo.com has IPv6 address 2001:4998:44:41d::3
yahoo.com has IPv6 address 2001:4998:c:1023::5
yahoo.com mail is handled by 1 mta6.am0.yahoodns.net.
yahoo.com mail is handled by 1 mta7.am0.yahoodns.net.
yahoo.com mail is handled by 1 mta5.am0.yahoodns.net.
```
```bash
root@ubuntu:~# cat /etc/hosts

127.0.0.1	    localhost
12.23.34.45	    google.com

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
```

### DNS query lookup order:
* `/etc/hosts`
* `/etc/resolv.conf`

**netstat:**
```bash
netstat # Print network connections, routing tables, interface statistics
netstat -a # Display all open ports & connections
netstat -at # all tcp
netstat -au # all udp
netstat -lt # Display Listening connections (only servers) TCP
netstat -lu # Display Listening connections (only servers) UDP
netstat -ltp # Listening tcp connections with their used programs
netstat -tulpn # List numeric
```

**ss:**
```bash
ss -a # all
ss -l # list 
ss -t # list tcp connections
ss -at # list all tcp connections
ss -lt # listening tcp connections
ss -u # list UDP connections
ss -au # all UDP
ss -lu # listening UDP
ss -ntlp
ss -nulp
```

**lsof:**

```bash
lsof # List open files
lsof -u USERNAME 
lsof -i TCP:22
lsof -i TCP:1-1024
lsof -i # all network connections
```

**nmap:**
> `Nmap` is a network exploration tool and security / port scanner 
```bash
nmap -v IP/DOMAIN
nmap localhost
nmap -v 192.168.80.139 192.168.80.140 ....
nmap 192.168.80.* # Scan range of IP
nmap 192.168.80.139,140,223
nmap 192.168.80.139-250
nmap 192.168.80.* --exclude 192.168.80.139
nmap -iL ip.txt # Scan list of host from file 
nmap -A 192.168.80.139 # Information OS and traceroute 
nmap -O 192.168.80.139 # Information OS
nmap -sA 192.168.80.139 # Scan IP for detect firewall 
nmap -PN 192.168.80.139 # Check IP for protected with firewall
nmap -F 192.168.80.139 # Fast scan 
nmap --iflist # Interface and route 
nmap -p T:80 192.168.80.139 # Scan tcp port
nmap -sU 53 192.168.80.139 # Scan UDP port 
```


