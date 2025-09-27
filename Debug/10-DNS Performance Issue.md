# DNS Performance Issue

### Issue:
> Response time is higher than usual

### Troubleshoot:
```sh
ab -n 2000 -c 200 http://192.168.122.100/users  # Test
# Response is 5 Seconds with no failed request
curl -XGET http://192.168.122.100/users
time curl -XGET http://192.168.122.100/users # Response in 3 Seconds
# Test without EndPoint:
curl -XGET http://192.168.122.100 # Response is better
time curl -XGET http://192.168.122.100 # Faster

sar 1 # There is no iowait
ss -s # Socket status is normal
ss -lntp # Normal
htop # Normal , no load
sar -n TCP 1 # High Passive & Active Connections
ps -aux --sort=-%cpu | head -n 10 # There is a process with high CPU usage (A Python Script)
```
```sh
# Check Nginx Configuration:
ls /etc/nginx/sites-enable/ # Nothing
ls /etc/nginx/conf.d/
less /etc/nginx/conf.d/api.conf # There is a config file here
# Nginx has a proxy to port 8080 to Python API.
```
```sh
# Checking the Python Script:
less data/api.py
# It is getting users count from a database server.
```
```sh
# Checking Database Server:
sar 1 # Normal 
htop # Normal
sar -n TCP 1 # Normal
```
```sh
# Checking Database:
mysql
show databases;
use db1,
show tables;
select count(*) from users;
52233
# Fast Response
```
```sh
# Test API<=>DB connectivity performance:
ping APIServer # Fast response
iperf3 -s # On Database Server
iperf3 -c DBServer # On API Server
# Connectivity performance is normal
```
```sh
ping db.local.net # Slow response with FQDN
dig +short db.local.net # Communication error on port 53, but resolved
# Going to wrong dns server address
```
```sh
vim /etc/resolv.conf # There is 2 DNS servers
nameserver 192.168.122.2
nameserver 192.168.122.1
dig +short db.local.net @DNS1 # Timeout
dig +short db.local.net @DNS2 # Get response
```

### Solution:
> Reorder NameServers
> Comment the NameServer which is unreachable



