# Security Scripts:

### Ubuntu Basic Security:
```sh
# ubuntu_basic_security.sh
#!/bin/bash
# ===========================================
# Basic Security Setup for Ubuntu 24.04
# ===========================================

echo "[+] Updating system packages..."
sudo apt update && sudo apt -y upgrade

echo "[+] Installing basic security tools..."
sudo apt install -y ufw fail2ban unattended-upgrades apt-listchanges

echo "[+] Disabling root SSH login and password authentication..."
sudo sed -i 's/^#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
sudo sed -i 's/^#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart sshd

echo "[+] Setting up UFW firewall..."
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw --force enable

echo "[+] Enabling automatic security updates..."
sudo dpkg-reconfigure -plow unattended-upgrades

echo "[+] Enabling fail2ban..."
sudo systemctl enable --now fail2ban

echo "[+] Basic security hardening completed."
```

### Ubuntu Users Logs:
```sh
# ubuntu_users_logs.sh
#!/bin/bash
# ===========================================
# User & Log Security Setup for Ubuntu 24.04
# ===========================================

echo "[+] Checking current users..."
awk -F: '{print $1}' /etc/passwd

echo "[+] Enforcing password policies..."
sudo apt install -y libpam-pwquality
sudo bash -c 'cat > /etc/security/pwquality.conf <<EOF
minlen = 10
minclass = 3
maxrepeat = 3
EOF'

echo "[+] Installing and configuring logwatch..."
sudo apt install -y logwatch
sudo logwatch --detail Low --mailto root --range today

echo "[+] Setting up logrotate..."
sudo systemctl enable logrotate.timer

echo "[+] User and log security setup completed."
```

### Ubuntu Monitoring Hardening:
```sh
# ubuntu_monitoring_hardening.sh
#!/bin/bash
# ===========================================
# Monitoring & System Hardening - Ubuntu 24.04
# ===========================================

echo "[+] Installing AIDE (file integrity checker)..."
sudo apt install -y aide
sudo aideinit
sudo mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db

echo "[+] Applying kernel hardening parameters..."
sudo bash -c 'cat > /etc/sysctl.d/99-hardening.conf <<EOF
kernel.randomize_va_space=2
net.ipv4.conf.all.rp_filter=1
net.ipv4.conf.all.accept_redirects=0
net.ipv4.conf.all.send_redirects=0
EOF'
sudo sysctl -p /etc/sysctl.d/99-hardening.conf

echo "[+] Installing Lynis for security auditing..."
sudo apt install -y lynis

echo "[+] Running Lynis scan..."
sudo lynis audit system

echo "[+] Monitoring and hardening setup completed."
```

### Rocky Basic Security:
```sh
# rocky_basic_security.sh
#!/bin/bash
# ===========================================
# Basic Security Setup for Rocky Linux 9
# ===========================================

echo "[+] Updating system packages..."
sudo dnf -y update

echo "[+] Installing basic security tools..."
sudo dnf install -y firewalld fail2ban dnf-automatic

echo "[+] Disabling root SSH login and password auth..."
sudo sed -i 's/^#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
sudo sed -i 's/^#PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart sshd

echo "[+] Enabling firewalld..."
sudo systemctl enable --now firewalld
sudo firewall-cmd --set-default-zone=public
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload

echo "[+] Enabling SELinux enforcing mode..."
sudo setenforce 1
sudo sed -i 's/^SELINUX=.*/SELINUX=enforcing/' /etc/selinux/config

echo "[+] Enabling automatic security updates..."
sudo systemctl enable --now dnf-automatic.timer

echo "[+] Basic security hardening completed."
```

### Rocky Users Logs:
```sh
# rocky_users_logs.sh
#!/bin/bash
# ===========================================
# User & Log Security Setup for Rocky Linux 9
# ===========================================

echo "[+] Checking current users..."
awk -F: '{print $1}' /etc/passwd

echo "[+] Enforcing password policy..."
sudo bash -c 'cat > /etc/security/pwquality.conf <<EOF
minlen = 10
minclass = 3
maxrepeat = 3
EOF'

echo "[+] Installing logwatch..."
sudo dnf install -y logwatch
sudo logwatch --detail Low --mailto root --range today

echo "[+] Enabling auditd for security logging..."
sudo dnf install -y audit
sudo systemctl enable --now auditd

echo "[+] User and log security setup completed."
```

### Rocky Monitoring Hardening:
```sh
# rocky_monitoring_hardening.sh
#!/bin/bash
# ===========================================
# Monitoring & System Hardening - Rocky Linux 9
# ===========================================

echo "[+] Installing AIDE for file integrity checking..."
sudo dnf install -y aide
sudo aide --init
sudo mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz

echo "[+] Applying kernel hardening parameters..."
sudo bash -c 'cat > /etc/sysctl.d/99-hardening.conf <<EOF
kernel.randomize_va_space=2
net.ipv4.conf.all.rp_filter=1
net.ipv4.conf.all.accept_redirects=0
net.ipv4.conf.all.send_redirects=0
EOF'
sudo sysctl -p /etc/sysctl.d/99-hardening.conf

echo "[+] Installing Lynis for auditing..."
sudo dnf install -y lynis

echo "[+] Running Lynis audit..."
sudo lynis audit system

echo "[+] Monitoring and hardening setup completed."
```







