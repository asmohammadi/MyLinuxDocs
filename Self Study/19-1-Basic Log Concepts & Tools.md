# Basic Log Concepts & Tools:


### Main Log Path:
* `/var/logs`
* `/var/log/syslog` : General System Logs
* `/var/log/auth.log` : Authentication & SSH Logs
* `/var/log/kern.log` : Kernel Messages
* `/var/log/dmesg` : Hardware Messages & System Boot
* `/var/log/faillog` : Failed Logins
* `/var/log/apt` : Packages Install/Update Reports 

### Outputs:
* `stdout` : Standard Output
* `stderr` : Standard Error
```sh
ls /root > out.log 2> err.log
# Normal logs going to out.log
# Error logs going to err.log
```

### Syslog:
* `Facility` : Source of logs (auth, daemon, cron)
* `Severity` : Priority of logs (info, warning, err, crit)
```sh
auth.info # User login information
daemon.err # System service error
```
```sh
# Syslog Structure:
# Severity + Facility
Aug 16 19:55:43 ubuntu sshd[1234]: Failed password for root from 192.168.1.50 port 45123 ssh2
# Auth error log
```

### Severity/Priority of logs:
* `debug`   : 7 - Troubleshooting Apps
* `info`    : 6 - Information
* `notice`  : 5 - Important but not error
* `warning` : 4 - Warning
* `err`     : 3 - Errors
* `crit`    : 2 - Critical Errors
* `alert`   : 1 - Need emegency action
* `emerg`   : 0 - System Failed/Unusable


### Journal & SystemD:
* In new OS (Ubuntu 24.04) services send their logs to systemd journal
* `Journalctl` will use to see the logs
```sh
journalctl # Display all logs
journalctl -n 20 # Display last 20 lines
journalctl -f # Realtime logs (tail -f)
journalctl -u ssh # Display logs of a Service
journalctl -b # Display logs from last Boot
journalctl -p warning # Display just warnings
journalctl -p err -b # Show just error logs after the last boot
journalctl --since "2025-07-13" --until "2025-07-13 15:00" # Display logs with date
journalctl --list-boots # Display reboot logs
journalctl -b -1 # Display last boot logs
journalctl | grep -i error # Search a key word in logs
```

### Logger:
> `logger` is a tool for sending a test message to syslog/journal
```sh
logger "This is a test log from Asghar"
# The message will save in /var/log/syslog & will show with journalctl
```




