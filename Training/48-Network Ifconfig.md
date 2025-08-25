# 48-Network Ifconfig

**ifconfig:**
```bash
ifconfig # Display Up Interfaces
ifconfig -a # Display all the Interfaces
ifconfig -s # Display short list
ifconfig eth0 172.16.43.155 netmask 255.255.255.224 # Add IP & Netmask.
ifconfig eth0 up/down # Set Up/Down the Interface
ifconfig del eth0 172.16.43.155 # Delete IP address
```
```bash
root@server:~# ifconfig -s # Netstat -i

Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
ens36            1500      153      0      0 0           139      0      0      0 BMRU
ens37            1500       36      0      0 0            36      0      0      0 BMRU
lo              65536       84      0      0 0            84      0      0      0 LRU
```

**ifup / ifdown:**
```bash
ifup ens37
ifdown ens37
```







