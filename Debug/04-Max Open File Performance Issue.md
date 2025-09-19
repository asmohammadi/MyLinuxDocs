# Max Open File Performance Issue:

### Apache Benchmark:
> `ab` is a tool for testing web server performance by sending requests.
```sh
ab -n 1000000 -c 1000 http://192.168.122.100/
# Send 1 Million request with 1000 concurrency to the endpoint
```

### Troubleshooting:
```sh
ab -n 10000 -c 1000 http://192.168.122.100/
# Getting error: Connection reset by peer
ab -n 10000 -c 500 http://192.168.122.100/ # This time working
```
```sh
htop
sar 1 # When running the Apache Benchmark tool it shows a load on CPU
sar -n TCP 1 # There is a network connection load when running AB command
ss -atn '( sport=80 )' | awk '{ print $1 }' | sort | uniq -c 1
# Display and count open & used ports
```
```sh
tail -f /var/log/nginx/error.log # Get error: "too many open files."
```
```sh
# Check the limitation of open files in Nginx: (Tuning the Nginx)
pidof nginx # Display nginx PIDs
cat /proc/152717/limits # Get the limitation info of the PID
```
### Solution:
```sh
vim /etc/nginx/nginx.conf # Edit Nginx configuration
# Enable rate limit of open file:
-> worker_rlimit_nofile 65535
#Increase the number of concurrent requests:
-> worker_connections 2048
nginx -t
systemctl reload nginx
```
```sh
# Change limitation from client-side to send more requests for test:
ulimit -n
ulimit -n 65535
```
```sh
# Test again with more concurrent requests:
ab -n 10000 -c 2000 http://192.168.122.100/ # Get error again
```
### Troubleshooting:
```sh
dmesg # Display kernel logs
# Error: Out of memory -- consider tunning tcp_mem
# Error: net_ratelimit
sysctl -a | grep -i tcp_mem
-> net.ipv4.tcp_mem = 22266     29690   44532
# The number of connections to this OS is more than the limitation, that kernel allowed for tcp_mem
```
### Solution:
```sh
sysctl -w net.ipv4.tcp_mem="222660 296900 445320" # Change the limitation of tcp_mem
# Test again:
ab -n 10000 -c 2000 http://192.168.122.100/ # No Error
ab -n 10000 -c 3000 http://192.168.122.100/ # No Error
```


