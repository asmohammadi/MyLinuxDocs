# Beats (file, metric, packet)

### Installing Beats:
```sh
apt install filebeat metricbeat packetbeat
```

### 1. Filebeat configuration:
```sh
# /etc/filebeat/filebeat.yml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/*.log

setup.kibana:
  host: "http://localhost:5601"
  username: "elastic"
  password: "your_password"

output.elasticsearch:
  hosts: ["localhost:9200"]
  username: "elastic"
  password: "3l9wJ7wec*rffj-6gjXg"

output.logstash:
  hosts: ["localhost:5044"]
```

### 2. Metricbeat configuration:
* Manual Modules Configuration
* Automatic Modules configuration

```sh
# Manual Modules Configuration:
# /etc/metricbeat/metricbeat.yml
metricbeat.modules:
- module: system
  metricsets:
    - cpu
    - memory
    - network
    - process
  enabled: true
  period: 10s
  processes: ['.*']

setup.kibana:
  host: "http://localhost:5601"
  username: "elastic"
  password: "your_password"

# Enable Elasticsearch just for the first time indexing, then disable it.
output.elasticsearch:
  hosts: ["localhost:9200"]
  username: "elastic"
  password: "3l9wJ7wec*rffj-6gjXg"

# Enable Logstash after indexing.
output.logstash:
  hosts: ["localhost:5044"]
```
```sh
# Automatic Modules configuration
# Modules Path: "/etc/metricbeat/modules.d/"
metricbeat modules enable system # Enable System module

# # /etc/metricbeat/metricbeat.yml
metricbeat.config.modules:
  # Glob pattern for configuration loading
  path: ${path.config}/modules.d/*.yml

setup.kibana:
  host: "http://localhost:5601"
  username: "elastic"
  password: "your_password"

# Enable Elasticsearch just for the first time indexing, then disable it.
output.elasticsearch:
  hosts: ["localhost:9200"]
  username: "elastic"
  password: "3l9wJ7wec*rffj-6gjXg"

# Enable Logstash after indexing.
output.logstash:
  hosts: ["localhost:5044"]
```

### 3. Packetbeat configuration:
```sh
# /etc/packetbeat/packetbeat.yml
packetbeat.interfaces.device: any
packetbeat.protocols:
- type: http
- type: dns

setup.kibana:
  host: "http://localhost:5601"
  username: "elastic"
  password: "your_password"

# Enable Elasticsearch just for the first time indexing, then disable it.
output.elasticsearch:
  hosts: ["localhost:9200"]
  username: "elastic"
  password: "3l9wJ7wec*rffj-6gjXg"

# Enable Logstash after indexing.
output.logstash:
  hosts: ["localhost:5044"]
```

```sh
# Enable Beats:
systemctl enable filebeat metricbeat packetbeat
systemctl start filebeat metricbeat packetbeat
systemctl status filebeat metricbeat packetbeat
systemctl restart filebeat metricbeat packetbeat
```

### Enable Beats Dashboard:
* Creating Mapping index & Kibana index
* Adding dashboards
```sh
filebeat setup --dashboards
metricbeat setup --dashboards
packetbeat setup --dashboards
```

### Index Beats:
```sh
filebeat setup
metricbeat setup
packetbeat setup
```
```sh
# Test Indexing:
curl -u elastic:ElasticPassword -X GET "http://localhost:9200/_cat/indices?v"
# Test Data Streams:
curl -u elastic:ElasticPassword -X GET "http://localhost:9200/_data_stream?pretty"
```

