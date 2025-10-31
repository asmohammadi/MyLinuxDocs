# Zimbra LDAP:

```sh
zmprov ga ali@zimbra.com all # Get Account

zmlocalconfig -s zimbra_ldap_password # Get password

# Get zimbra Configuration:
ldapsearch -x -H ldap://mail.zimbra.com -D "uid=zimbra,cn=admins,cn=zimbra" -W -b "cn=config,cn=zimbra" "(objectClass=zimbraGlobalConfig)"

# Show all Domains:
ldapsearch -x -H ldap://mail.zimbra.com -D "uid=zimbra,cn=admins,cn=zimbra" -W -b '' "(objectClass=zimbraDomain)"

# Show all Active Users:
ldapsearch -x -H ldap://mail.zimbra.com -D "uid=zimbra,cn=admins,cn=zimbra" -W -b '' "(&(objectClass=zimbraAccount)(zimbraAccountStatus=active))" mail displayName zimbraMailHost

# Search specific user:
ldapsearch -x -H ldap://mail.zimbra.com -D "uid=zimbra,cn=admins,cn=zimbra" -W -b '' "(mail=ali@example.com)"

# Get Distribution Lists:
ldapsearch -x -H ldap://mail.zimbra.com -D "uid=zimbra,cn=admins,cn=zimbra" -W -b '' "(objectClass=zimbraDistributionList)"

# Just show DNs:
ldapsearch -x -LLL -b '' "(objectClass=zimbraAccount)" dn

# Search just one level:
ldapsearch -x -s one -b '' "(objectClass=*)"

ldapsearch -x -LLL -H ldap://mail.zimbra.com -D "uid=zimbra,cn=admins,cn=zimbra" -W -b "cn=accounts,cn=zimbra" "(mail=ali@zimbra.com)" dn

ldapsearch -x -LLL -H ldap://mail.zimbra.com -D "uid=zimbra,cn=admins,cn=zimbra" -W -b "uid=ali,cn=accounts,cn=zimbra" -s base "(objectClass=*)" '*' '+'
```

```sh
ldapsearch -x -LLL -H ldap://mail.zimbra.com -D "uid=zimbra,cn=admins,cn=zimbra" -W -b '' -s base "(objectClass=*)" '*' '+'
```
* `-x` : Simple Authentication
* `-H` : Set Host
* `-LLL` : Clear output, without Header & Comment
* `-D` : DN of the Admin user
* `-w` : Password
* `-W` : Request password
* `-s` : No subtree
* `+` , `*` : All attributes(Normal & Operational)
* `-s base` : Search one level
* `-s sub` : Search recursive


```sh
# Object Class is Account & the "zimbraMailSieveScript" attribute has value:
(&(objectClass=zimbraAccount)(zimbraMailSieveScript=*))

ldapsearch -x -LLL -H ldap://mail.zimbra.com -D "uid=zimbra,cn=admins,cn=zimbra" -W  -b '' -s sub  "(&(objectClass=zimbraAccount)(zimbraMailSieveScript=*))"  mail cn sn displayName givenName > /tmp/sieve_users.ldif
```
```sh
# Output to csv file with column header:
ldapsearch -x -H ldap://localhost -D "cn=config" -w <password> \
  "(&(objectClass=zimbraAccount)(zimbraSieveEnabled=TRUE))" \
  mail givenName sn cn | \
awk '
BEGIN {
    FS=": "; OFS=",";
    print "mail,givenName,sn,cn";
}
$1=="mail"{mail=$2}
$1=="givenName"{givenName=$2}
$1=="sn"{sn=$2}
$1=="cn"{cn=$2}
$1=="dn" && NR>1 {
    print mail, givenName, sn, cn;
    mail=givenName=sn=cn="";
}
END {
    print mail, givenName, sn, cn;
}' > sieve_users.csv
```

```sh
# Get all attributes of an ObjectClasses:
ldapsearch -x -H ldap://localhost -D "uid=zimbra,cn=admins,cn=zimbra" -W -b "cn=schema" "(objectClass=*)" \
  objectClasses | grep -A 10 "zimbraAccount"

```
```sh
# Get the name of all attributes:
ldapsearch -x -H ldap://localhost -D "uid=zimbra,cn=admins,cn=zimbra" -W -b "cn=schema" "(objectClass=*)" objectClasses | \
awk '/zimbraAccount/,/^\)/' | grep -Eo '\$[[:space:]]*[a-zA-Z0-9_-]+' | tr -d '$ ' | sort -u
```

```sh
# Get the name of all ObjectClasses:
ldapsearch -x -H ldap://localhost -D "uid=zimbra,cn=admins,cn=zimbra" -W -b "cn=schema" "(objectClass=*)" objectClasses | \
grep "NAME" | sed -E 's/.*NAME[[:space:]]+\x27([^']+)\x27.*/\1/' | sort -u
```

```sh
# Display all Schema:
slapcat -n 0 | grep -A 20 "zimbraAccount"
slapcat -n 0 -F /opt/zimbra/data/ldap/config/cn\=config
```


