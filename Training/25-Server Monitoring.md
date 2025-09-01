# 25-Server Monitoring
 
**Monitoring Tools:**
* `ps`
* `pgrep`
* `top`
* `htop`
* `btop`
* `jobs`
* `kill`
* `signal`
* `pkill`
* `free`
* `uptime`

**System Monitoring:**
* `stress-ng`
* `vmstat`
* `sar`
* `iotop`

**Network Monitoring:**
* `ifconfig`
* `netstat`
* `iftop`
* `nload`
* `iptraf-ng`
* `iperf`

### PS:
```sh
ps # Process Status
ps -aux
ps -aux | grep init # All processes with `init`.
ps -aux | grep init | grep -v grep # Except the `grep`.
```
* `a` = show processes for all users
* `u` = display the process’s user/owner
* `x` = also show processes not attached to the terminal

```sh
root@server:~# ps
    PID TTY          TIME CMD
   1472 pts/0    00:00:00 bash
   2147 pts/0    00:00:00 ps
```
```sh
root@server:~# ps -aux | head -10
USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root          1  0.0  0.3 185244  3856 ?        Ss   Oct11   0:07 /sbin/init auto noprompt
root          2  0.0  0.0      0     0 ?        S    Oct11   0:00 [kthreadd]
root          4  0.0  0.0      0     0 ?        I<   Oct11   0:00 [kworker/0:0H]
root          6  0.0  0.0      0     0 ?        I<   Oct11   0:00 [mm_percpu_wq]
root          7  0.0  0.0      0     0 ?        S    Oct11   0:12 [ksoftirqd/0]
root          8  0.0  0.0      0     0 ?        I    Oct11   0:19 [rcu_sched]
root          9  0.0  0.0      0     0 ?        I    Oct11   0:00 [rcu_bh]
root         10  0.0  0.0      0     0 ?        S    Oct11   0:00 [migration/0]
root         11  0.0  0.0      0     0 ?        S    Oct11   0:01 [watchdog/0]
```
### pgrep:
```bash
pgrep sleep # Show the process ID with `sleep`.
pgrep -c sleep # Count processes with `sleep`.
pgrep -a sleep # Show full processes with their commands.
pgrep -n sleep # Show the newest process with `sleep`.
pgrep -P sleep # Show the parent process.
```
```sh
root@server:~# sleep 100 &
[1] 2230
root@server:~# sleep 200 &
[2] 2231
root@server:~# sleep 300 &
[3] 2232
root@server:~# sleep 400 &
[4] 2233
root@server:~# sleep 500 &
[5] 2234
root@server:~# pgrep sleep
2230
2231
2232
2233
2234
```

### Top:
```bash
top # Realtime Process Monitoring
```
```sh
Tasks: 237 total,   1 running, 174 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.8 us,  0.4 sy,  0.0 ni, 98.7 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :   985080 total,   167700 free,   501856 used,   315524 buff/cache
KiB Swap:  1045500 total,   448216 free,   597284 used.   256968 avail Mem 

   PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND    
 59562 root      20   0   41952   3604   2920 R 12.5  0.4   0:00.02 top        
     1 root      20   0  185244   3856   2244 S  0.0  0.4   0:07.76 systemd    
     2 root      20   0       0      0      0 S  0.0  0.0   0:00.01 kthreadd   
     4 root       0 -20       0      0      0 I  0.0  0.0   0:00.00 kworker/0:+
     6 root       0 -20       0      0      0 I  0.0  0.0   0:00.00 mm_percpu_+
     7 root      20   0       0      0      0 S  0.0  0.0   0:12.88 ksoftirqd/0
     8 root      20   0       0      0      0 I  0.0  0.0   0:19.92 rcu_sched  
     9 root      20   0       0      0      0 I  0.0  0.0   0:00.00 rcu_bh     
    10 root      rt   0       0      0      0 S  0.0  0.0   0:00.00 migration/0
```
**%CPU**:
* `us` : User space
* `sy` : System space
* `ni` : Not idle
* `id` : Idle
* `wa` : Wait
* `hi` : Hardware interupt
* `si` : Software interupt
* `st` : 

**Short Keys**:
* `d` : Set delay time for refresh
* `z` : Set colour
* `c` : Command path
* `k` : Kill process with ID
* `M` : Sort by memory usage
* `P` : Sort by CPU usage
* `h` : Help
* `1` : Show Split CPUs
* `ltm1` : Show CPU & Memory usage with buffer & percentage
* `q` : Exit

**htop:**

> Like top but colourized and better view.

**btop:**

> Like top & htop but newer version and better view.

**Jobs:**
```bash
jobs # Show background process.
jobs -l # Show background process with PIDs.
```
```sh
root@server:~# sleep 1000 &
[1] 32476
root@server:~# sleep 2000 &
[2] 32477
root@server:~# sleep 3000 &
[3] 32478
root@server:~# sleep 4000 &
[4] 32480
root@server:~# jobs
[1]   Running                 sleep 1000 &
[2]   Running                 sleep 2000 &
[3]-  Running                 sleep 3000 &
[4]+  Running                 sleep 4000 &
root@server:~# jobs -l
[1]  32476 Running                 sleep 1000 &
[2]  32477 Running                 sleep 2000 &
[3]- 32478 Running                 sleep 3000 &
[4]+ 32480 Running                 sleep 4000 &
```
**kill:**
```bash
kill PID # Stop a process with PID
```
```sh
root@server:~# jobs -l
[1]  32476 Running                 sleep 1000 &
[2]  32477 Running                 sleep 2000 &
[3]- 32478 Running                 sleep 3000 &
[4]+ 32480 Running                 sleep 4000 &
root@server:~# kill 32477
root@server:~#
[2]   Terminated              sleep 2000
```
**Signal:**
```bash
kill -s SignalName PID
kill -n SignalNumber PID
kill -9 32478
```
* `SIGINT` # 2 -> Interupt `Ctrl + d`
* `SIGQUIT` # 3 -> Quit `Ctrl + d`
* `SIGKILL` # 9 -> Quit immediately
* `SIGTERM` # 15 -> Terminate process (Default kill)

```bash
killall sleep
```
```sh
root@server:~# killall sleep
[3]-  Terminated              sleep 3000
[4]+  Terminated              sleep 4000
```
**pkill:**
```bash
pkill sleep # Kill all sleep process.
```
```sh
root@server:~# pkill sleep
[2]-  Terminated              sleep 200
[1]-  Terminated              sleep 100
[3]+  Terminated              sleep 300
```

**free:**
```bash
free # Show Memory Usage
free -h # Human readable
free -m # In Megabyte
free -g # In Gigabytes
free -t # Total
```
```sh
root@ubuntu16-1:~# free
              total        used        free      shared  buff/cache   available
Mem:         985080      432716      135464       16724      416900      339484
Swap:       1045500      671864      373636
```
```sh
root@ubuntu16-1:~# free -h
              total        used        free      shared  buff/cache   available
Mem:           961M        423M        128M         16M        410M        330M
Swap:          1.0G        655M        365M
```
**uptime:**
```bash
uptime # Show Uptime & Load Average (Based on CPU cores & IO)
```
```sh
root@ubuntu16-1:~# uptime 
 03:37:00 up 3 days, 19:07,  1 user,  load average: 0.00, 0.00, 0.00

root@server:~# uptime 
 12:10:01 up 45 min,  2 users,  load average: 0.08, 0.07, 0.12
```
* `0.08` load average of last 1 minute
* `0.07` load average of last 5 minute
* `0.12` load average of last 15 minute

Load average based on cpu and io

For example if you use 1 cpu:
* load average `0.5` means => half used :)
* load average `1.0` means => fully used :|
* load average `1.5` means => overused :(

### Extra Monitoring Tools:
* `stress-ng`: Load on CPU, Memory, IO, Network & Disk.
* `sysstat`
* `iotop` : Check i/o but it's not a real-time.
* `nload` : Network Load
* `ifconfig`
* `iftop` : Network
* `iperf` : Bandwidth
* `net-tools`
* `iptraf-ng`

### System Monitoring Tools:
**stress-ng:**
```bash
stress-ng -c 1 # Use 100% of one core cpu.
stress-ng -m 2 # Load on Memory
stress-ng --hdd 1 # Load on Hard Disk
```
**vmstat:**
```bash
vmstat # Sysstat tool, Show virtual memory usage
```
```sh
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 1162320  27124 535700    0    0    24    60   28   38  0  0 100  0  0
```
**sar:**
```bash
sar # iotop tool, check i/o.
sar 1 10 # Checking i/o every 1 second and 10 repeat.
```
```sh
root@server:~# sar 1 10
Linux 5.4.0-107-generic (ubuntu-srv) 	08/12/2022 	_x86_64_	(4 CPU)

12:31:41 PM     CPU     %user     %nice   %system   %iowait    %steal     %idle
12:31:42 PM     all      0.00      0.00      0.00      0.00      0.00    100.00
12:31:43 PM     all      0.00      0.00      0.00      0.00      0.00    100.00
12:31:44 PM     all      0.00      0.00      0.25      0.00      0.00     99.75
12:31:45 PM     all      0.00      0.00      0.00      0.00      0.00    100.00
12:31:46 PM     all      0.00      0.00      0.00      0.00      0.00    100.00
12:31:47 PM     all      0.00      0.00      0.00      0.00      0.00    100.00
12:31:48 PM     all      0.00      0.00     16.67     36.72      0.00     46.61
12:31:49 PM     all      0.00      0.00      3.38     75.32      0.00     21.30
12:31:50 PM     all      0.00      0.00      2.84     76.23      0.00     20.93
12:31:51 PM     all      0.00      0.00      5.48     68.41      0.00     26.11
Average:        all      0.00      0.00      2.79     25.09      0.00     72.12
```
**iotop:**
```bash
iotop # Show Disk I/O.
```
### Network Monitoring Tools:
**ifconfig:**
```bash 
ifconfig # Show TX & RX of an Interface.
```
```sh
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.137.128  netmask 255.255.255.0  broadcast 192.168.137.255
        inet6 fe80::20c:29ff:fefc:9072  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:fc:90:72  txqueuelen 1000  (Ethernet)
        RX packets 286858  bytes 398213903 (398.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 104170  bytes 7084606 (7.0 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
**netstat:**
```bash
netstat -ie # To to see interface status and information.
netstat -s # Show send & receive details of an Inteface based on protocols.
netstat -r # Show Routing table.
netstat -ntlp # Show open ports.
```
```sh
Kernel Interface table
ens33: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.137.128  netmask 255.255.255.0  broadcast 192.168.137.255
        inet6 fe80::20c:29ff:fefc:9072  prefixlen 64  scopeid 0x20<link>
        ether 00:0c:29:fc:90:72  txqueuelen 1000  (Ethernet)
        RX packets 286919  bytes 398219397 (398.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 104220  bytes 7090426 (7.0 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
**iftop:**
```bash
iftop # Live Network Monitoring Tool.
```
**nload:**
```bash
nload # Show Interface Send & Receive.
nload -m # Display all Interfaces
```
**iptraf-ng:**
```bash
iptraf-ng # Show Interface traffic Graphically.
iptraf-ng -i InterfaceName
```
**iperf:**
```bash
iperf # A Clinet-Server tool for checking speed between two linux systems.
iperf -s # Make device Server & listening to Client.
iperf -c ServerIP # Make device Client & connect to Server.
```
