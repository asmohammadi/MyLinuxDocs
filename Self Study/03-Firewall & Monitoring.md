# Firewall & Monitoring.md

### Firewall:

```bash
ufw status
ufw enable/disable
ufw allow 22/tcp
ufw allow 80/tcp
ufw deny 23
ufw delete allow 80/tcp # Delete a firewall rule
```

### Iptables:
> Ubuntu 24.04 uses `nftable`.

```bash
iptables -L -v # List all firewall Rules (Input, Output, Forward)
iptables -L -v --line-numbers
iptables -A INPUT -p tcp --dport 8080 -j ACCEPT # Any connection to port 8080 accepted.
iptables -A INPUT -p tcp --dport 23 -j DROP # Any connection to port 23 will drop.
iptables -D INPUT 2 # Delete a firewall rule with Rule Number.
iptables -F # Delete all firewall rules.
iptables -A INPUT -s 1.2.3.4 -j DROP # Drop IP Address
iptables -A INPUT -s 192.168.1.0/24 -j DROP # Drop IP Range
iptables -A INPUT -s 1.2.3.4 -j ACCEPT # Accept IP Address
iptables -A INPUT -j DROP # Accept just the IP above
```
```bash
root@ubuntu:~# iptables -L -v --line-numbers

Chain INPUT (policy ACCEPT 123 packets, 10234 bytes)
num   pkts bytes target     prot opt in     out     source          destination
1       20  1500 DROP       all  --  *      *       1.2.3.4         0.0.0.0/0
2       50  4000 ACCEPT     tcp  --  *      *       anywhere        anywhere        tcp dpt:2222
3       10   800 DROP       tcp  --  *      *       192.168.1.0/24  0.0.0.0/0       tcp dpt:80
```

> All iptables configurations are Temporary and its better to use `nftables` or `iptables-persistent`.

### Saving Iptables Configurations:
```bash
iptables-save > /etc/iptables.rules # Save Rules in new file
nano /etc/systemd/system/iptables-restore.service # Create a SystemD Service

# Put these lines in SystemD Service:
[Unit]
Description=Restore iptables rules
Before=network-pre.target
Wants=network-pre.target

[Service]
Type=oneshot
ExecStart=/sbin/iptables-restore < /etc/iptables.rules
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
# Save the SystemD Service 

# Activate Iptables configuration:
systemctl daemon-reexec
systemctl enable iptables-restore
```

### Monitoring:

#### Netdata:
> `Netdata` is a real-time monitoring tool.
```bash
# Install NetData:
wget -O /tmp/netdata-kickstart.sh https://get.netdata.cloud/kickstart.sh && sh /tmp/netdata-kickstart.sh
# Netdata Dashboard:
http://your_server_ip:19999
```

**Netdata COnfiguration:**
> `/etc/netdata/netdata.conf`
```bash
chown netdata /etc/netdata/ssl/private.key
chown netdata /etc/netdata/ssl/server.crt
# Netdata Self-signed Certificate Configuration:
   [web]
       mode = static
       web directory = /usr/share/netdata/web
       ssl certificate = /etc/netdata/ssl/server.crt
       ssl key = /etc/netdata/ssl/private.key
       ssl verify client = no
       enable = yes
       port = 19999
       address = 192.168.64.128
```

#### Cockpit:
> `Cockpit` is web-based complete monitoring tool for daily reports.
```bash
apt install cockpit -y # Install Cockpit
systemctl enable --now cockpit.socket # Enable Cockpit
ufw allow 9090/tcp # Open firewall port for Cockpit
```

### Basic CLI Monitoring Tools (Ubuntu)

- `top`     : Real-time view of system processes and resource usage.
- `htop`    : Enhanced version of `top` with color and interactive UI.
- `df -h`   : Show disk space usage in a human-readable format.
- `free -h` : Display available and used memory (RAM) in human-readable format.
- `uptime`  : Show how long the system has been running and current load average.
- `vmstat`  : Report memory, CPU, and I/O stats.
- `iostat`  : Show CPU and disk I/O statistics.
- `dstat`   : Versatile resource usage statistics (requires installation).






