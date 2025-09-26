# Performance Issue for Service Dependency

### Issue:
> Response time is higher than usual in a period of time(30 Days)

### Troubleshoot:
```sh
ab -n 2000 -c 200 http://192.168.122.100/users  # Test
# Response time is 2.5 Seconds
curl -XGET http://192.168.122.100/users
time curl -XGET http://192.168.122.100/users
# Tsets without EndPoint:
curl -XGET http://192.168.122.100 # Response is better
time curl -XGET http://192.168.122.100 # Faster

sar 1 # There is no iowait
sar -n TCP 1 # High Passive & Active Connections
ss -s # Socket status is normal
ss -lntp # Normal
htop # Normal , no load
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
sar 1 # High load on User usage
sar -n TCP 1 # High Passive Connections, No Active Connections
htop # High CPU Load
watch -n1 vmstat -s # Memory is normal
sar -b 1 # Block Device is normal
```

* `Passive` : Connections from outside to server
* `Active` : Connection from Server to Outside

```sh
# Checking Database:
mysql
show databases;
use db1,
show tables;
select count(*) from users;
52233
# High Response to answer
```

