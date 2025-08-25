# Kibana

### Installing Kibana:
```sh
# Add Repository:
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | gpg --dearmor -o /usr/share/keyrings/elastic.gpg
echo "deb [signed-by=/usr/share/keyrings/elastic.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | tee /etc/apt/sources.list.d/elastic-8.x.list
# Install Kibana:
apt update
apt install kibana
# Enable Service:
systemctl enable kibana
systemctl start kibana
systemctl status kibana
```

### Kibana configuration:
```sh
nano /etc/kibana/kibana.yml
# Set these:
server.port: 5601
server.host: "0.0.0.0"   # Or server IP
elasticsearch.hosts: ["https://localhost:9200"]

# If needed Username / Password:
elasticsearch.username: "kibana_system"
elasticsearch.password: "Password"

# To disregard the validity of SSL certificates, change this setting's value to 'none'.
elasticsearch.ssl.verificationMode: none
```

### Configuring Kibana User & Password:
1. ElasticSearch + Kibana on the same server
2. ElasticSearch & Kibana on different servers

#### 1. On the same server:
* Reset `kibana_system` password
* Use the password in kibana config file
```sh
# Reset password for Kibana service account: (kibana_system)
/usr/share/elasticsearch/bin/elasticsearch-reset-password -u kibana_system
# Edit Kibana config file:
nano /etc/kibana/kibana.yml
# Add these:
elasticsearch.hosts: ["https://localhost:9200"]
elasticsearch.username: "kibana_system"
elasticsearch.password: "kibana_system_password"
elasticsearch.ssl.verificationMode: none
```

#### 2. On different servers:
* Enroll token for `kibana` connection with ElasticSearch
* Reset `kibana_system` password
* Use the password in kibana config file
```sh
# Enrollment token for Kibana user: (Expire after 30 Min)
/usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
```

### Test Kibana:
```sh
journalctl -u kibana -f
tail -f /var/log/kibana/kibana.log
```










