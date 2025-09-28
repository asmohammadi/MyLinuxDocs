# Kill Process - Memory Performance Issue

### Issue:
> An API service has been killed with no response.


### Troubleshoot:
```sh
curl http://192.168.122.100 # Failed to connect
echo > /dev/tcp/192.168.122.100/80 # Connection refused
ss -ltnp # Nginx port not shown
systemctl status nginx.service # Service failed : "oom-kill"
systemctl start nginx.service
ss -ltnp
ab -n 500000 -c 5000 http://192.168.122.100 # Test
dmesg -D # Error: Out of memory: killed process 825 (nginx)
```

* `oom-kill` : Out of memory killer, kill a process

```sh
# oom-kill will decide on a rate:
ps aux | grep -i nginx
cat /proc/825/oom_
oom_adj     oom_score       oom_score-adj
```

```sh
vmstat -s # Check memory
htop # High memory usage
ps aux --sort=-%mem | head -n 10
# There is a python script that uses memory
cat /proc/800/oom_score_adj # Get the score rate of the python script process
-1000
# So it will remain working
```

