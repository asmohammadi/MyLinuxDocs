# Server Port Response Issue:

### Scenario:
> Client requests to API Server has been failed with no response.

### Troubleshoot:

```sh
# On Client:
ping 192.168.150.110(APIServerIP)
telnet 192.168.150.110 22
echo > /dev/tcp/192.168.150.110/22 # Same as Telnet
echo > /dev/tcp/192.168.150.110/80 # Test API port has been failed with no response
```
```sh
# On API Server:
tcpdump -i any tcp port 80 -n # Check receiving request fro Client on port 80
# The request from Client has been received on API Server
nft list ruleset # Check iptable
```
```sh
# On Client:
nft list ruleset 
tracepath -n 192.168.150.110 # There is a hub between Client & API Server
mtr -n # Same as trace with packet lost
tcpdump -i any host 192.168.150.110 and port 80 -n # On the middle Router
echo > /dev/tcp/192.168.150.110/80 # On Client
# There is no issue for sending request, on the Router
nft list ruleset # On the Router
# There is a Drop Rule on iptable of Router for API Server IP Address.
```

### Solution:
* Disabling the NFT Rule
* Restart the nftable.service

```sh
# Test:
curl -I -L http://192.168.150.110 # It's OK.
```

### NFT Rules Script:
```sh
sudo sysctl -w net.ipv4.ip_forward=1
sudo nft add table ip nat
sudo nft add chain ip nat prerouting { type nat hook prerouting priority -100 \; }
sudo nft add chain ip nat postrouting { type nat hook postrouting priority 100 \; }
sudo nft add rule ip nat postrouting oifname "enp1s0" iifname "enp7s0" masquerade

sudo nft add table ip filter
sudo nft add chain ip filter forward { type filter hook forward priority 0 \; }
sudo nft add rule ip filter forward ip saddr 192.168.150.110 tcp sport 80 drop
```












