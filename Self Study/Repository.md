# Repository:

### Change Repository:
```sh
sed -i 's|http://ir.archive.ubuntu.com/ubuntu|http://archive.ubuntu.com/ubuntu|g' /etc/apt/sources.list.d/ubuntu.sources
```

```sh
# Repository Files:
/etc/apt/sources.list.d/
/etc/apt/sources.list.d/ubuntu.sources
/etc/apt/sources.list.d/docker.list
/etc/apt/sources.list.d/ansible-ubuntu-ansible-noble.sources
```

```sh
# Security Repository:
http://security.ubuntu.com/ubuntu/
```

### RedHat/Rocky Linux Repository:
```sh
/etc/yum.repos.d/
```
```sh
dnf repolist # Show all repositories
dnf update # Update repository package list
```
```sh
# Remove Zabbix Repository:
dpkg -purge zabbix-release
```



