# Elasticsearch

### Installing Elasticsearch:
```sh
# Prerequisites:

# Set descriptor limit:
nano /etc/security/limits.conf
# Add:
elasticsearch  -  nofile  65536
elasticsearch  -  nproc   4096

# Turn off Swap:
swapoff -a

# Enable Firewall port:
Elasticsearch : 9200 (Http)
Transport : 9300
```
```sh
# Add Repository:
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | tee /etc/apt/sources.list.d/elastic-8.x.list
```
```sh
apt update
apt install elasticsearch
```
```sh
# Enable Service:
systemctl enable --now elasticsearch
```
```sh
# Test:
curl -u elastic:Password http://localhost:9200
curl -k https://localhost:9200
username: elastic
password: autogenerate (3l9wJ7wec*rffj-6gjXg)
```
```sh
# Config file:
/etc/elasticsearch/elasticsearch.yml
# Extra configuration:
/etc/elasticsearch/elasticsearch.yml.d/
# Java config:
/etc/elasticsearch/jvm.options

# Data path:
/var/lib/elasticsearch
# Log path:
/var/log/elasticsearch
```
```sh
# Disable security:
xpack.security.enabled: false # Add to "elasticsearch.yml"
# Reset password:
/usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
# Create enrollment token for Kibana:
/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
# Create enrollment token for Elasticsearch nodes:
/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node
```

### ElasticSearch Configuration:
```sh
# Enable security:
xpack.security.enabled: true
xpack.security.enrollment.enabled: true
# Disable SSL
xpack.security.http.ssl:
  enabled: false
xpack.security.transport.ssl:
  enabled: false
http.host: 0.0.0.0
```
```sh
sed -i 's|xpack.security.enabled: true|xpack.security.enabled: false|g' /etc/elasticsearch/elasticsearch.yml
```

### Test ElasticSearch & Connection with Kibana:
```sh
curl -u elastic:YourElasticPass https://127.0.0.1:9200
curl -u elastic:YourElasticPass http://127.0.0.1:9200 --insecure
curl -k -u elastic:YourElasticPass http://127.0.0.1:9200
curl -k -u elastic:YourElasticPass https://127.0.0.1:9200
curl -u kibana_system:Password https://localhost:9200/
curl -u kibana_system:Password http://localhost:9200/ --insecure
curl -u kibana_system:Password https://localhost:9200/ --cacert /etc/elasticsearch/certs/http_ca.crt
```

### Change Passwords Using API:
```sh
curl -u elastic:<ElasticPassword> -X POST "https://localhost:9200/_security/user/kibana_system/_password" \
  -H 'Content-Type: application/json' \
  -d '{"password": "NewKibanaPass"}' \
  --cacert /etc/elasticsearch/certs/http_ca.crt
```






