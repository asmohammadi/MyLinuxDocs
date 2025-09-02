# Node Exporter

### Node Exporter:

```sh
# Install Node Exporter:
cd /tmp
curl -LO https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-amd64.tar.gz # Get file
tar xvf node_exporter-1.8.2.linux-amd64.tar.gz # Extract file
mv node_exporter-1.8.2.linux-amd64/node_exporter /usr/local/bin/ # Move binary files
useradd -rs /bin/false nodeusr # Create a user for Node Exporter
# Create a SystemD Service:
nano /etc/systemd/system/node_exporter.service
# Add these lines:
-----
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=nodeusr
Group=nodeusr
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=default.target
-----
# Enable & Run the Service:
systemctl daemon-reload
systemctl enable node_exporter
systemctl start node_exporter
systemctl status node_exporter
```
```sh
curl http://localhost:9100/metrics
```









