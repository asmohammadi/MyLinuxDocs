# Bind DNS:

### Bind DNS:
```sh
apt-get install bind9 dnsutils bind9-docs # Install Bind
/etc/bind # Bind installing directory
/etc/bind/named.conf # Bind configuration (Configuration files paths)
/etc/bind/named.conf.options
/etc/bind/named.conf.local # Where to add Zones and Zone Database files paths

```
```sh
/etc/init.d/bind9 start # Starting Bind service
/etc/bind/rndc reload # Reload the DNS Cache Service 
```
```sh
/etc/bind/db.domain.local # Forward Lookup Zone Database File Configuration
/etc/bind/db.1.168.192 # Reverse Lookup Zone Database File Configuration:
```
#### Cache-only DNS:
```sh
vim /etc/bind/named.conf.options:
# To enable Cache-only DNS add this to the end of file:
recursion yes;
```
```sh
# /etc/bind/named.conf.local:

// Do any local configuration here
//

// Consider adding the 1918 zones here, if they are not used in your
// organization
//include "/etc/bind/zones.rfc1918";

zone    "domain.net" {
        type    master;
        file "etc/bind/db.domain.net";
};
zone    "1.168.192.in-addr.arpa" {
        type    master;
        file "etc/bind/db.1.168.192";
};
```
#### Primary DNS:
```sh
# /etc/bind/named.conf.local:
# Secondary DNS: 192.168.0.11
zone    "domain.net" {
        type    master;
        file "etc/bind/db.domain.net";
        allow-transfer { 192.168.1.11; };
};
zone    "1.168.192.in-addr.arpa" {
        type    master;
        file "etc/bind/db.1.168.192";
};
```
#### Slave DNS (Secondary DNS):
```sh
# /etc/bind/named.conf:
# Primary DNS: 192.168.1.10
zone    "domain.net" {
        type    slave;
        file "etc/bind/db.domain.net";
        masters { 192.168.1.10; };
};
zone    "1.168.192.in-addr.arpa" {
        type    slave;
        file "etc/bind/db.1.168.192";
};
```
