# DNS:

### Secure DNS:

#### DNSSEC:
```sh
# Generate a Key for securing DNS servers connection:
dnssec-keygen -a HMAC-MD5 -b 128 -n HOST rndc-key
* `-a` : Algorithm
* `-b` : Bite
* `-n` : Name Type
```

#### TSIG:
```sh
# Create TSIG Key file on Master DNS Server::
/etc/bind/tsig.key
# Add Slave DNS:
server 192.168.0.11 {
        keys { TRANSFER; };
 };


# Adding TSIG file path to bind configuration on Master DNS Server:
/etc/bind/named.conf

include "/etc/bind/tsig.key";


# Creating TSIG Key file on Slave DNS Server:
/etc/tsig.key
# Add MAster DNS:
server 192.168.0.10 {
        keys { TRANSFER; };
 };


# Adding TSIG file path to bind configuration on Slave DNS Server:
/etc/bind/named.conf

include "/etc/tsig.key";
```



