# Grafana

### Install Grafana:
```sh
# Add official Repository
apt-get install -y apt-transport-https software-properties-common wget
mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | tee /etc/apt/keyrings/grafana.gpg > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | tee /etc/apt/sources.list.d/grafana.list
# Install Grafana:
apt-get update
apt-get install grafana -y
# Enable & Running Grafana:
systemctl enable grafana-server
systemctl start grafana-server
systemctl status grafana-server
```
```sh
# Grafana dashboard:
http://<IP-Server>:3000
Username: admin
Password: admin
```

### Connecting Grafana to Prometheus:

```sh
# Add Prometheus as Data Source to Grafana:
Grafana Dashboard > Connections > Data Sources > Add data source > Prometheus
# Add Prometheus URL:
http://<IP-Server>:9090
```

### Grafana Custom Dashboard:
```sh
# Example Query:
node_cpu_seconds_total
node_memory_MemAvailable_bytes
node_network_receive_bytes_total
```












