# Simple Checklist:

# ✅ Simple Checklist:

---

## 🔐 SSH Security
- [ ] Generate SSH key pair (RSA or ED25519)
- [ ] Copy public key to server
- [ ] Disable password-based SSH login
- [ ] Change default SSH port (22)
- [ ] Install and configure Fail2Ban

---

## 👥 User & Permissions
- [ ] Create a new user with `adduser`
- [ ] Add user to `sudo` group
- [ ] Edit and verify `/etc/sudoers`
- [ ] Test sudo access

---

## 🔥 Firewall & Access Control
- [ ] Install and enable UFW
- [ ] Allow required ports (22, 80, 443, etc.)
- [ ] Test remote access
- [ ] Block specific IPs or ranges using `iptables`

---

## 🔒 SSL & Certificates
- [ ] Install Certbot and web server plugins
- [ ] Issue SSL certificate using Let’s Encrypt
- [ ] Enable and test HTTPS access
- [ ] Set up auto-renewal using systemd timer or cron
- [ ] Reload web server after renewal

---

## 💾 Backup & Cron Jobs
- [ ] Create rsync backup script with logging
- [ ] Test backup manually with `--dry-run`
- [ ] Schedule backups via `cron`
- [ ] Test restore from backup




