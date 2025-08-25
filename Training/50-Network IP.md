# 50-Network IP

**IP:**
> `IP` is a new command for `ifconfig`.

```bash
ip command example | description
-------------------| -----------
ip address show # show all IP addresses associated on all network devices
ip address show eth0 # Display the information of an interface
ip addr add 192.168.50.5/24 dev eth0 # Assign an IP Address to a specific Interface
ip addr del 192.168.50.5/24 dev eth0 # Remove an IP Address
ip link show # Display Network Interface(s)
ip link set eth0 up # Enable Interface
ip link set eth0 down # Disable Interface
ip route show # Show routing table information
ip route add 10.10.20.0/24 via 192.168.50.100 dev eth0 # Add a static route
ip route del 10.10.20.0/24 # Remove static route
```
> All the above settings are **`Not Permanent`**

**ping:**

```bash
ping -n # Numeric output only. Do not try to resolve hostname
ping -i Interval # Wait interval seconds between sending each packet
ping -i 3 # Wait 3 seconds
ping -I Interface # Set source address to specified interface address
ping -I eth0 8.8.8.8
ping -c 3 # Reply 3 time. 
ping6 # For IPv6
```



