# Advance Search in Logs

### Tools for Searching in Logs:
* tail
* grep
* awk
* sed
* cut

```sh
# Simple search in log:
grep "error" /var/log/nginx/error.log
# Case-insensitive search:
grep -i "failed" /var/log/auth.log
# Search in multi files:
grep "sshd" /var/log/*
```
```sh
# Process logs & extract columns:
awk '{print $1,$2,$3}' /var/log/syslog
# Counting logs based on IP:
awk '{print $11}' /var/log/nginx/access.log | sort | uniq -c | sort -nr
```
```sh
# Replace or delete a text:
sed -n '/error/p' /var/log/syslog # Only lines include error
```
```sh
# Extract specific part of a log:
cut -d' ' -f1 /var/log/nginx/access.log | sort | uniq -c | sort -nr
```

### Piping: (Combination of tools)
```sh
# Find the number of failed logins:
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr

# Display the first 10 IP addresses with the most errors:
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head -10

# List users who has more failed logins:
grep "Failed password" /var/log/auth.log | awk '{print $(NF-5)}' | sort | uniq -c | sort -nr

# All Nginx errors in last 24 hours:
grep "$(date --date='1 day ago' '+%b %e')" /var/log/nginx/error.log | grep "error"
```

### Real-time monitoring
```sh
# Display sshd logs in real-time:
journalctl -u ssh.service -f
# Multiple logs concurrently & colorized:
multitail /var/log/syslog /var/log/auth.log # Need "multitail" tool
```

### Sample:
```sh
# Find today's failed services logs:
journalctl --since today -p err
```








