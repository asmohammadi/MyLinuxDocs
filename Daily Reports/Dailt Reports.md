# Daily Reports:


For a **Linux administrator**, daily reports usually focus on **system health, services, resources, and security**. These reports help to detect potential issues early and ensure services run smoothly. Categorized, the daily reports can include:


### **1. System Health**

* **Resource Usage:**

  * RAM and Swap (`free -h`, `vmstat`, `top`, `htop`)
  * CPU (`top`, `mpstat`, `sar`)
  * Disk I/O (`iostat`, `iotop`)
* **Partition Usage:**

  * Used and free space (`df -h`)
  * Inode usage (`df -i`)
  * Directory sizes for critical paths (`du -sh /var/log /home /etc`)

---

### **2. Logs and Events**

* **System & Kernel Logs:**

  * `/var/log/syslog` or `/var/log/messages`
  * Kernel warnings/errors (`dmesg`)
* **Service Logs:**

  * Apache/Nginx logs (`/var/log/nginx/access.log`, `error.log`)
  * Database logs (MySQL/MariaDB/PostgreSQL)
* **Login Attempts:**

  * SSH logs (`/var/log/auth.log`)
  * Check for failed or suspicious logins (`lastb`, `journalctl -u ssh`)

---

### **3. Services and Processes**

* Check status of critical services (`systemctl status servicename`)
* Monitor heavy or unusual processes (`ps aux --sort=-%mem,-%cpu`)
* List active and enabled services (`systemctl list-units --type=service --state=running`)

---

### **4. Network and Security**

* Network connections (`ss -tuln`, `netstat -tulnp`)
* Network bandwidth and traffic (`iftop`, `nload`)
* Firewall and iptables checks (`ufw status`, `iptables -L`)
* Monitor important system file changes (`auditd`, `tripwire`, or `diff` for sensitive files)

---

### **5. Backups and Databases**

* Verify successful backup executions (`rsync`, `tar`, `mysqldump`)
* Check database sizes and integrity

---

### **6. Automated Monitoring**

* Using monitoring tools such as:

  * `Nagios`, `Zabbix`, `Prometheus` for automatic checks
  * Email or SMS alerts for errors or high resource usage

---

### **7. Summary and Reporting**

* Prepare a **short daily report** including:

  * Resource usage
  * Services that went down or restarted
  * Critical log errors
  * Security warnings
  * Backup status

These reports are usually saved as a simple text file, CSV, or automatically emailed to senior management.





