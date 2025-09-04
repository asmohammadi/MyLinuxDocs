# Keepalived

* Load balance
* High Availability
* Using VRRP (Virtual Router Redundancy Protocol)
* Active / Backup Router
* Using Virtual IP

### Install KeepAlived:
```sh
# On both Keepalived servers:
apt install keepalived
# Enable VRRP:
nano /etc/default/keepalived
# Add vrrp:
DEAMON_ARGS="--vrrp"
```

### Keepalived Configuration:
```sh
# On bot Keepalived Servers:
# Edit config file:
nano /etc/keepalived/keepalived.conf
# Configuration On MASTER Keepalived Server:
global_defs {
        router_id node01
}

vrrp_instance router {
        state MASTER
        interface eth0
        virtual_router_id 1
        priority 110
        advert_int 1
        
        authentication {
                auth_type PASS
                auth_pass 12345
        }

        virtual_ipaddress {
                192.168.10.10 # Must be reserved as Virtual IP
        }

        track_interface {
                eth0
        }
}

# Configuration On BACKUP Keepalived Server:
global_defs {
        router_id node02
}

vrrp_instance router {
        state BACKUP
        interface eth0
        virtual_router_id 1
        priority 100
        advert_int 1
        
        authentication {
                auth_type PASS
                auth_pass 12345
        }

        virtual_ipaddress {
                192.168.10.10 # Must be reserved as Virtual IP
        }

        track_interface {
                eth0
        }
}
```
```sh
keepalived -t # Check configuration before running
systemctl enable --now keepalived # Run Keepalived service
```

### Install HaProxy on both Keepalived Servers:
```sh
# Installing HaProxy & Configure it on both servers:
apt install haproxy
```



