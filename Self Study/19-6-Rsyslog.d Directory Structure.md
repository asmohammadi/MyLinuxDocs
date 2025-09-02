# Rsyslog.d Directory Structure

### Enterprise Structure:

```sh
/etc/rsyslog.d/
├── 01-modules.conf             # Load core modules (imuxsock, imjournal, imtcp, gtls, etc.)
├── 02-global.conf              # Global settings (workDirectory, queues, defaults)
│
├── 10-input-ssl.conf           # Secure TLS/SSL input (port 6514)
├── 11-input-udp.conf           # UDP input (if required)
├── 12-input-tcp.conf           # Plain TCP input (if required)
│
├── 20-filters-syslog.conf      # Filters for system logs (auth, kernel, cron, etc.)
├── 21-filters-nginx.conf       # Filters for nginx logs
├── 22-filters-apache.conf      # Filters for apache logs
├── 23-filters-mysql.conf       # Filters for mysql/mariadb logs
├── 24-filters-sshd.conf        # Filters for sshd logs
│
├── 30-rules-routing.conf       # Routing rules (send each log type to proper destinations)
├── 31-rules-severity.conf      # Severity-based rules (e.g., only warning and above for audit)
│
├── 40-storage-local.conf       # Local disk storage (/var/log/host/service.log)
├── 41-storage-nfs.conf         # NFS-mounted storage
│
├── 50-forward-central.conf     # Forward logs to central log server (TLS)
├── 51-forward-backup.conf      # Forward logs to backup server (failover)
│
├── 60-rotation.conf            # Log rotation (integration with logrotate)
├── 61-retention.conf           # Retention policy (e.g., keep logs for 90 days)
│
├── 70-alerts.conf              # Alerts (e.g., failed SSH login → email/slack)
├── 71-intrusion-detection.conf # IDS rules (regex patterns for brute-force attempts, etc.)
│
└── 99-debug.conf               # Debug/Testing configuration (enable/disable quickly)
```

### 📌 Explanation of Each Section:

* `01–09 → Core`
Core modules and global configs.
* `10–19 → Inputs`
Define input sources (SSL/TCP/UDP). In production, usually only 10-input-ssl.conf is enabled.
* `20–29 → Filters`
Per-service filters (nginx, apache, mysql, sshd, etc.).
* `30–39 → Rules`
Routing and severity rules (decide where logs go and what severity levels to keep).
* `40–49 → Storage`
Define where logs are stored (local disk, NFS).
* `50–59 → Forwarding`
Forward logs to central/backup servers (with TLS).
* `60–69 → Rotation/Retention`
Log rotation and retention policies.
* `70–79 → Alerts/IDS`
Define alerts or simple intrusion detection patterns.
* `90–99 → Debug/Custom`
Debug configs or project-specific customizations.









