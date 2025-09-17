# Daily Reports Script:

This script covers:
* System resources (CPU, memory, disk)
* Logs (syslog, SSH failed attempts)
* Running services and top processes
* Network and firewall status
* Basic backup check

```sh
crontab -e
# Schedule: Every day at 08:00 AM
0 8 * * * /home/username/daily_system_report.sh
```

```sh
#!/bin/bash
# Daily Linux System Report Script
# File: daily_system_report.sh

# --- Settings ---
REPORT_DIR="$HOME/system_reports"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
REPORT_FILE="$REPORT_DIR/daily_report_$TIMESTAMP.txt"

# Create report directory if it doesn't exist
mkdir -p "$REPORT_DIR"

# --- Header ---
echo "===============================" > "$REPORT_FILE"
echo "Daily System Report - $TIMESTAMP" >> "$REPORT_FILE"
echo "===============================" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# --- 1. System Health ---
echo "1. System Health" >> "$REPORT_FILE"
echo "-----------------" >> "$REPORT_FILE"

echo "CPU Usage:" >> "$REPORT_FILE"
top -bn1 | head -5 >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "Memory Usage:" >> "$REPORT_FILE"
free -h >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "Disk Usage:" >> "$REPORT_FILE"
df -h >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "Top 10 Largest Directories in /var/log:" >> "$REPORT_FILE"
du -h /var/log 2>/dev/null | sort -hr | head -10 >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# --- 2. Logs and Events ---
echo "2. Logs and Events" >> "$REPORT_FILE"
echo "------------------" >> "$REPORT_FILE"

echo "Recent Syslog Errors (last 50 lines):" >> "$REPORT_FILE"
tail -n 50 /var/log/syslog 2>/dev/null | grep -i "error" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "SSH Failed Login Attempts (last 20 lines):" >> "$REPORT_FILE"
tail -n 20 /var/log/auth.log 2>/dev/null | grep "Failed password" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# --- 3. Services and Processes ---
echo "3. Services and Processes" >> "$REPORT_FILE"
echo "--------------------------" >> "$REPORT_FILE"

echo "Active Services:" >> "$REPORT_FILE"
systemctl list-units --type=service --state=running >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "Top 10 CPU/Memory Processes:" >> "$REPORT_FILE"
ps aux --sort=-%mem,-%cpu | head -10 >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

# --- 4. Network and Security ---
echo "4. Network and Security" >> "$REPORT_FILE"
echo "------------------------" >> "$REPORT_FILE"

echo "Listening Ports:" >> "$REPORT_FILE"
ss -tuln >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "Firewall Status:" >> "$REPORT_FILE"
ufw status >> "$REPORT_FILE" 2>/dev/null
echo "" >> "$REPORT_FILE"

# --- 5. Backups (example check) ---
echo "5. Backups" >> "$REPORT_FILE"
echo "-----------" >> "$REPORT_FILE"

# Example: check last backup timestamp (adjust path if needed)
if [ -d "/backup" ]; then
    echo "Last backup files:" >> "$REPORT_FILE"
    ls -lh /backup | tail -10 >> "$REPORT_FILE"
else
    echo "Backup directory /backup not found." >> "$REPORT_FILE"
fi
echo "" >> "$REPORT_FILE"

# --- Footer ---
echo "Report Generated Successfully." >> "$REPORT_FILE"
echo "===============================" >> "$REPORT_FILE"

# Optional: print report path
echo "Report saved to: $REPORT_FILE"
```







