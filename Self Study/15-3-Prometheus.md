# Prometheus

### Install Prometheus:
```sh
cd /tmp
curl -LO https://github.com/prometheus/prometheus/releases/download/v2.54.1/prometheus-2.54.1.linux-amd64.tar.gz # Get file
tar xvf prometheus-2.54.1.linux-amd64.tar.gz # Extract files
# Moving files:
mv prometheus-2.54.1.linux-amd64/prometheus /usr/local/bin/
mv prometheus-2.54.1.linux-amd64/promtool /usr/local/bin/
mkdir /etc/prometheus
mv prometheus-2.54.1.linux-amd64/prometheus.yml /etc/prometheus/
mv prometheus-2.54.1.linux-amd64/consoles /etc/prometheus/
mv prometheus-2.54.1.linux-amd64/console_libraries /etc/prometheus/
# Create a specific user for Prometheus:
useradd --no-create-home --shell /bin/false prometheus
chown -R prometheus:prometheus /etc/prometheus
mkdir /var/lib/prometheus
chown prometheus:prometheus /var/lib/prometheus
# Create a SystemD service:
nano /etc/systemd/system/prometheus.service
# Add these lines:
------
[Unit]
Description=Prometheus Monitoring
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
ExecStart=/usr/local/bin/prometheus \
  --config.file=/etc/prometheus/prometheus.yml \
  --storage.tsdb.path=/var/lib/prometheus/ \
  --web.console.templates=/etc/prometheus/consoles \
  --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target
------
# Enable & run Service:
systemctl daemon-reload
systemctl enable prometheus
systemctl start prometheus
systemctl status prometheus
```
```sh
http://localhost:9090
```

### Connect Node Exporter to Prometheus:
```sh
# Edit Prometheus config file:
nano /etc/prometheus/prometheus.yml
# Edit scrape_configs:
-----
scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "node_exporter"
    static_configs:
      - targets: ["localhost:9100"]
-----
# Restart Prometheus:
systemctl restart prometheus
# Test in browser:
http://localhost:9090/targets
```

### Discovery Methods for Enterprise Networks:
1. File-based Service Discovery
   * Saving servers IP addresses in another file and add it in prometheus config file.
```sh
# prometheus.yml:
scrape_configs:
  - job_name: "nodes"
    file_sd_configs:
      - files:
        - "targets.json"

# target.json file: (List of all servers)
[
  {
    "targets": ["192.168.1.101:9100", "192.168.1.102:9100", "192.168.1.103:9100"],
    "labels": { "job": "node" }
  }
]
```

2. DNS-based Service Discovery
   * Discover from DNS records (A record & CNAME)
3. Cloud Service Discovery
   * Azure, AWS, Kubernetes, ...
   * Using their API and discover servers automatically







