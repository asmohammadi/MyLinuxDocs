# Swap:

### Swappiness:
> `vm.swappiness` is a value for how much using swap on a system.
> The value is between 0 to 100.
> More value means use more swap rather than Memory.
```sh
cat /proc/sys/vm/swappiness # Check swappiness value
sysctl vm.swappiness=10 # Change the value
# For permanent need to add to:
/etc/sysctl.conf
```

### smem:
```sh
apt install smem
smem -rs swap # Display the swap usage of each process
```

### Check Swap Using Scrip:
```sh
# Display the first 20 process with more swap usage:
for pid in $(ls /proc | grep '^[0-9]*$'); do
  sw=$(grep VmSwap /proc/$pid/status 2>/dev/null | awk '{print $2}')
  if [ "$sw" != "" ] && [ "$sw" -ne 0 ]; then
    echo "PID=$pid swap=${sw}KB $(ps -p $pid -o comm=)"
  fi
done | sort -k3 -nr | head -20
```

#### Colorized Script:
```sh
#!/bin/bash
# لیست ۲۰ پروسه اول با بیشترین swap به همراه RAM و اسم پروسه

printf "%-8s %-10s %-10s %-s\n" "PID" "SWAP(KB)" "RSS(KB)" "COMMAND"
for pid in $(ls /proc | grep '^[0-9]*$'); do
    if [ -r /proc/$pid/status ]; then
        swap=$(awk '/VmSwap/ {print $2}' /proc/$pid/status)
        rss=$(awk '/VmRSS/ {print $2}' /proc/$pid/status)
        if [ "$swap" != "" ] && [ "$swap" -ne 0 ]; then
            cmd=$(ps -p $pid -o comm=)
            printf "%-8s %-10s %-10s %-s\n" "$pid" "$swap" "$rss" "$cmd"
        fi
    fi
done | sort -k2 -nr | head -20
```









