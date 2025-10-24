# LDAP & OpenLDAP

### Standards:
* `DAP` : Directory Access Protocol (OSI Model Base)
* `LDAP` : Lightweight Directory Access Protocol (TCP/IP Model Base)
* `OpenLDAP` : Service:Software
* `Active Directory` : Service:Software

### Structure:
```sh
# Distinguished Name:
uid=user,ou=location,dc=domain,dc=com
```
* `dc` : Directory Container
* `ou` : Organizational Unit
* `UID` : User Identifier

### Install OpenLDAP:
```sh
apt install slapd ldap-utils
dpkg-reconfigure slapd # Change Default domain name
DNS Domain Name:
Organization name: 
Administrator password: 
Confirm password:
Database format: HDB, BDB, MDB(Recommended)
```
```sh
# Configuration path:
/etc/ldap/
ldap.conf   sasl2   schema   slapd.d
```
```sh
slapcat
slapcat -b cn=config # Display LDAP configuration
```
```sh
slapadd -l import.ldif # ldif file is using to import & create a User
```

### LDIF File:
```sh
dn: ou=users,dc=domain,dc=com
objectClass: organizationalUnit

dn: uid=ali,ou=users,dc=domain,dc=com
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: shadowAccount
uid: ali
sn: ahmadi
givenName: ali
cn: ali
uidNumber: 2501
gidNumber: 2501
userPassword: pa$$w0rd
loginShell: bin/bash
homeDirectory: /home/ali
```

### LDAP Commands:
```sh
ldapsearch # Search & View
ldappasswd # Change Password
ldapadd # Add User
ldapdelete # Delete User
```
* `-h` : Set OpenLDAP Host
* `-x` : Simple authentication (like anonymous login)
* `-b` : Define base
* `-D` : Define distinguished name
* `-W` : Request password
* `-w` : Define password
* `-f` : Define file
* `-S` : Define user
```sh
ldapsearch -h localhost -x -D cn=admin,dc=domain,dc=com -W -b dc=domain,dc=com 
ldapsearch -h localhost -x -b dc=domain,dc=com dn: # Just display Distinguished names
ldappaswwd -h localhost -x -D cn=admin,dc=domain,dc=com -w P@ssw0rd -S uid=ali,ou=users,dc=domain,dc=com
ldapadd -h localhost -x -D cn=admin,dc=domain,dc=com -w P@ssw0rd -f ahmad.ldif 
ldapdelete -h localhost -x -D cn=admin,dc=domain,dc=com -w P@ssw0rd uid=ali,ou=users,dc=domain,dc=com
```

### sssd:
> `sssd` is using to communicate between `PAM` and `OpenLDAP` service.

```sh
# Add sssd to nsswitch configuration:
/etc/nsswitch.conf
passwd:     sssd compact systemd
```


