# Kernel Automation & Configuration:

```sh
systcl.conf # Permanent configuration file for loading kernel modules
/etc/sysctl.d/ # Packages loaded on kernel modules
/sbin/sysctl
/proc/sys/kernel # Current live kernel modules
udev # Monitoring live adding & removing kernel modules
lsusb # Display connected USB devices
lspci # Display connected PCI devices
lsdev # Display all connected system devices
dmesg # Logs of system devices
udevadm monitor # Real-time monitoring of kernel modules
/etc/modprobe.d/blacklist.conf # Not allow udev to install old kernel modules
```
```sh
root@server:~# ls /etc/sysctl.d/
10-bufferbloat.conf       10-ipv6-privacy.conf      10-magic-sysrq.conf
10-network-security.conf  10-zeropage.conf          README.sysctl
10-console-messages.conf  10-kernel-hardening.conf  10-map-count.conf
10-ptrace.conf            99-sysctl.conf
```

