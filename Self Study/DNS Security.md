# Secure DNS:

#### DNSSEC:
```sh
# Enable DNSSEC:
# /etc/bind/named.conf.options:

options {
    directory "/var/cache/bind";

    dnssec-enable yes;
    dnssec-validation auto;

    auth-nxdomain no;
    listen-on-v6 { any; };
};
```
```sh
# Create KSK(Key Signing Key):
dnssec-keygen -a RSASHA256 -b 2048 -f KSK yourdomain.com
# Output:
Kyourdomain.com.+008+26450.key
Kyourdomain.com.+008+26450.private

# Create ZSK(Zone Signing Key):
dnssec-keygen -a RSASHA256 -b 2048 yourdomain.com
# Output:
Kyourdomain.com.+008+50959.key
Kyourdomain.com.+008+50959.private
```
```sh
# Add keys to Zone files:
vim /etc/bind/zones/db.yourdomain.com
# Add to the end of file:
$INCLUDE "Kyourdomain.com.+008+26450.key"
$INCLUDE "Kyourdomain.com.+008+50959.key"
```
```sh
# Zone sign:
dnssec-signzone -A -3 $(head -c 1000 /dev/random | sha1sum | cut -b 1-16) \
    -N INCREMENT \
    -o yourdomain.com \
    -t db.yourdomain.com

# New zone file:
db.yourdomain.com.signed
```
```sh
# Change zone file configuration:
vim /etc/bind/named.conf.local

zone "yourdomain.com" {
    type master;
    file "/etc/bind/zones/db.yourdomain.com.signed";
    auto-dnssec maintain;
    inline-signing yes;
};
```
```sh
systemctl reload bind9
systemctl status bind9
```

#### TSIG:
```sh
# Generate a Key for securing DNS servers connection:
dnssec-keygen -a RSASHA256 -b 2048 -n HOST hostname.domain.net
* `-a` : Algorithm
* `-b` : Bite
* `-n` : Name Type
```
```sh
# Create TSIG Key file on Master DNS Server::
vim /etc/bind/tsig.key
# Add Slave DNS:
server 192.168.0.11 {
        keys { TRANSFER; };
 };

# Adding TSIG file path to bind configuration on Master DNS Server:
vim /etc/bind/named.conf

include "/etc/bind/tsig.key";

# Creating TSIG Key file on Slave DNS Server:
vim /etc/tsig.key
# Add MAster DNS:
server 192.168.0.10 {
        keys { TRANSFER; };
 };

# Adding TSIG file path to bind configuration on Slave DNS Server:
vim /etc/bind/named.conf

include "/etc/tsig.key";
```

### Chroot Jail:
```sh
/etc/default/bind9 # To enable chroot
```
```sh
# Edit Bind service to enable Chroot:
systemctl edit bind9

[Service]
ExecStart=
ExecStart=/usr/sbin/named -u bind -t /var/chroot/bind -c /etc/named.conf
```
```sh
# Create needed directories:
mkdir -p /var/chroot/bind/etc
mkdir -p /var/chroot/bind/var/cache/bind
mkdir -p /var/chroot/bind/var/log
mkdir -p /var/chroot/bind/var/run/named
```
```sh
# Copy needed files:
cp /etc/bind/* /var/chroot/bind/etc/
cp /etc/localtime /var/chroot/bind/etc/
cp /etc/resolv.conf /var/chroot/bind/etc/
```
```sh
# Set Permissions:
chown -R bind:bind /var/chroot/bind
chmod -R 755 /var/chroot/bind
```
```sh
# Fix AppArmor (Disable It for BIND in Chroot):
# AppArmor blocks chroot unless disabled for BIND
ln -s /etc/apparmor.d/usr.sbin.named /etc/apparmor.d/disable/
apparmor_parser -R /etc/apparmor.d/usr.sbin.named
```
```sh
# Restart Bind:
systemctl daemon-reload
systemctl restart bind9
```
```sh
# Verify Bind is running in Chroot:
ps aux | grep named
# Output:
/usr/sbin/named -u bind -t /var/chroot/bind
```
```sh
# Test configuration:
named-checkconf -t /var/chroot/bind
# Test zones:
named-checkzone example.com /var/chroot/bind/etc/example.com.zone
```



