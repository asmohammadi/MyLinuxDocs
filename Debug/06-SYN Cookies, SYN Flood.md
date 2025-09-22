# SYN Cookies, SYN Flood:

```sh
bash netstat.sh
watch -n1 -d "bash netstat.sh | grep -E -i 'syn|flow|drop'"
ss -ltn
bash ss.sh
```
```sh
sysctl -a | grep -E -i "somax|syn_backlog|cook"
net.core.somaxconn = 2048
net.ipv4.tcp_max_syn_backlog = 512
net.ipv4.tcp_syncookies = 1 # 0=Disable, 1=Enable when queue has overflow, 2=Enable anyway
```
```sh
# Enable SYN Cookie:
echo 1 > /proc/sys/net/ipv4/tcp_syncookies
# or:
sysctl -w net.ipv4.tcp_syncookies=1
```
```sh
# Test Flood:
hping3 -S --flood -p 80 192.168.122.100 # Syn_receive will increase
```

