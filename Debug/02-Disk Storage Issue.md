# Disk Storage Issue:

```sh
df -h
du -sh
ps aux | grep output.log | grep -v grep # See the process of the file
while true; do ps aux | grep output.log | grep -v grep; done # It will show if there is any open process for the file.
lsof output.log # Show the PID of the file
# Cause there is no process for output.log file, so if we delete the file it will create again.
watch -n 5 rm output.log # Delete the file every 5 second. It will keep the disk free till we solve the issue.
lsof output.log # Now we can see the process, because now disk has free space to write on the file.
while true; do ps aux | grep output.log | grep -E -v "grep|watch"; done # Again see no process
while true; do ps auxf | grep head | grep -v grep; done # Display process in tree view, to see the parent process
while true; do ps auxf | grep -B5 head | grep -v grep; done # Display 5 lines before the process
find / -type f -name io-write.sh # Find the sh file that is running the process
file /PATH/io-write.sh # Check the file information
ps aux | grep io-write.sh # Display the processes of the running file
ps -auxf | less # Display in forest(tree) mode
-> io-write.sh # Show the processes & parent processes
kill PID
```

## io-write.sh Script:
```sh
#!/bin/bash

output_file="/var/log/output.log"

chunk_size=10485760 

total_size=$((1000000 * 10485760))

iterations=$((total_size / chunk_size))

(
    for i in $(seq 1 "$iterations"); do
        head -c "$chunk_size" < /dev/zero >> "$output_file"
        sleep 0.1
    done
    while true; do sleep 1; done
) &
writer_pid=$!

sleep 2

rm -f "$output_file"

> "$output_file" 
(
    for i in $(seq 1 "$iterations"); do
        head -c "$chunk_size" < /dev/zero >> "$output_file"
        sleep 0.1
    done
) &

wait
```



