# AppArmor:

```sh
aa-status
systemctl status apparmor
sudo systemctl enable --now apparmor # Enable AppArmor
cat /sys/module/apparmor/parameters/enabled
```
### AppArmor Path:
```sh
/etc/apparmor/ # Config files
/etc/apparmor.d/ # Main Profiles
/etc/apparmor.d/local/ # Override profiles
/var/lib/apparmor/ # Profile Database (Old Version)
/var/cache/apparmor/ # Profiles cache
/sys/kernel/security/apparmor/ # AppArmor Running path in Kernel
/var/log/syslog # Logs
```

### Profiles Status:
* `Enforce` : Force to run & block
* `Complain` : No force, just log
* `Prompt`
* `Kill`
* `Unconfined`
* `Mixed`
* `Disables` : Disable

```sh
aa-enforce /etc/apparmor.d/usr.bin.nginx # Enable enforce
aa-complain /etc/apparmor.d/usr.bin.nginx # Enable complain
aa-disable /etc/apparmor.d/usr.bin.nginx
```

### Create Profile:
```sh
aa-genprof curl # Create profile for curl
# Run the App to analyze it:
curl https://google.com
# Suggesting the Rules:
[1] Allow read access to /etc/ssl/certs/* ?
(A)llow / (D)eny / (A)bstract / (I)gnore
```

### Check Logs:
```sh
journalctl -xe | grep apparmor
grep -i apparmor /var/log/syslog
grep -i DENIED /var/log/syslog
```
```sh
# AppArmor Log Example:
audit: apparmor="DENIED" operation="open" profile="/usr/bin/curl" name="/etc/shadow" ...
```



