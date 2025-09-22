# RAM & Swap Performance Issue:

```sh
# Test performance:
ab -n 100000 -c 5000 http://192.168.122.100/ 
# Time per request is higher than usual.
```
```sh
# Troubleshoot:
bash netstat.sh
watch -n1 -d "bash netstat.sh | grep -E -i 'synretrans|timewait|overflow|drop'"
bash ss.sh
ss -ltn
sar 1 # iowait is high
sar -n TCP 1 # Check network -> Normal
sar -b -d 1 10 # Check Block Device (Disk)
# There is high transactions on Disk.
iotop # Normal, No process for I/O on disks
vmstat -s # Check virtual memory, Swap, CPU & I/O status
vmstat --stat --unit=M # Human readable
watch -n1 vmstat --stat --unit=M # Display changes
```
### Issue:
> We have high SwapIn & SwapOut on disk, and engaged the I/O.

```sh
ps aux | head -n 10
ps aux --sort=%mem | head -n 10 # Sort by Memory
ps aux --sort=-%mem | head -n 10 # Sort reverse
# There is a Python Script that using Memory.
```

### Python Script:
```py
# mem.py

import numpy as np
import time

def utilize_memory(size_in_gb):
    
    # Allocate memory (convert GB to number of 64-bit elements)
    num_elements = size_in_gb * (1024**3) // 8
    memory_array = np.zeros(num_elements, dtype=np.float64)  # Use numpy to allocate memory in RAM

    for i in range(100000):  # Run some operations to keep memory busy
        memory_array += 1.0  # Modify the data to ensure it stays in RAM
        time.sleep(1)  # Pause briefly to simulate sustained usage

    print("Memory utilization complete. Keeping data in RAM for observation.")
    time.sleep(6000)  # Keep memory allocated for 10 minutes to observe usage

if __name__ == "__main__":
    try:
        size_in_gb = 2
        utilize_memory(size_in_gb)
    except MemoryError:
        print("Error: Not enough memory available to allocate the requested size.")
    except KeyboardInterrupt:
        print("Script interrupted by user.")
```

### Swappiness:
* `Swappiness` is the desire of kernel to using Swap.
* The value is between `0` to `100`.
* More value means more desire to use Swap.
 
```sh
sysctl -a | grep -i swap
vm.swappiness = 60
```

