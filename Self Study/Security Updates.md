# Security Updates:

```sh
apt install --only-upgrade package_name # Install the specific package
apt install ubuntu-advantage-tools # For CVE-specific fixes
pro fix CVE-XXXX-XXXX # Fix a specific CVE
# Installing only security updates:
apt list --upgradable | grep security
apt-get install -y --only-upgrade $( apt-get --just-print upgrade | awk 'tolower($4) ~ /.*security.*/ || tolower($5) ~ /.*security.*/ {print $2}' | sort | uniq )
```

```sh
apt list --installed | grep unattended-upgrades
apt install unattended-upgrades
# Configure automatic updates:
dpkg-reconfigure unattended-upgrades
nano /etc/apt/apt.conf.d/50unattended-upgrades # Edit the configuration file
"${distro_id}:${distro_codename}-security"; # Enable this line
# Upgrade only security updates: (Command-Line)
apt list --upgradable | grep security | cut -d/ -f1 | xargs sudo apt-get install -y
```




