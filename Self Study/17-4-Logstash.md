# Logstash

### Installing Logstash:
```sh
# Add Repository:
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | gpg --dearmor -o /usr/share/keyrings/elastic.gpg
echo "deb [signed-by=/usr/share/keyrings/elastic.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | tee /etc/apt/sources.list.d/elastic-8.x.list
# Install Logstash:
apt update
apt install logstash -y
# Enable Service:
systemctl enable logstash
systemctl start logstash
systemctl status logstash
```

### Logstash Configuration:
```sh
# Config file path:
/etc/logstash/conf.d/syslog.conf
```sh
# Config file structure:
input { }   # Receive log files, beats or syslog
filter { }  # Process & filter logs (Parsing, Grok)
output { }  # Sending to ElasticSearch, or file
```
```sh
# Config file sample:
input {
  beats {
    port => 5044
  }
}

filter {
  grok {
    match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{SYSLOGHOST:host} %{DATA:program}: %{GREEDYDATA:message}" }
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    user => "elastic"
    password => "YourElasticPass"
    index => "syslog-%{+YYYY.MM.dd}"
  }
  stdout { codec => rubydebug }
}
```
```sh
journalctl -u logstash -f
```

### Real Standard Logstash Config file:

* `Input` : Filebeat, Metricbeat, Packetbeat
* `Filter` : Process logs with grok (parse logs), mutate (standard columns & fields), date (timestamp)
* `Output` : ElasticSearch with Real SSL, with index setting, and stdout for debug

```sh
# /etc/logstash/conf.d/enterprise.conf
# ===================== INPUT =====================
input {
  # Filebeat
  beats {
    port => 5044
    ssl => true
    ssl_certificate => "/etc/logstash/certs/logstash.crt"      # SSL certificate purchased
    ssl_key => "/etc/logstash/certs/logstash.key"              # Private key
  }

  # Metricbeat
  beats {
    port => 5045
    ssl => true
    ssl_certificate => "/etc/logstash/certs/logstash.crt"
    ssl_key => "/etc/logstash/certs/logstash.key"
  }

  # Packetbeat
  beats {
    port => 5046
    ssl => true
    ssl_certificate => "/etc/logstash/certs/logstash.crt"
    ssl_key => "/etc/logstash/certs/logstash.key"
  }

  # Optional: Local syslog
  tcp {
    port => 10514
    type => syslog
  }
}

# ===================== FILTER =====================
filter {
  # Grok parsing for syslog-like messages
  if [type] == "syslog" {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{HOSTNAME:host} %{DATA:program}: %{GREEDYDATA:log_message}" }
    }
    date {
      match => [ "syslog_timestamp", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
      timezone => "UTC"
    }
  }

  # Mutate example: add fields, rename, remove
  mutate {
    add_field => { "environment" => "production" }
    rename => { "host" => "server_name" }
    remove_field => ["@version", "path"]
  }

  # Example: Metricbeat processing
  if [@metadata][beat] == "metricbeat" {
    mutate {
      add_field => { "source_type" => "metric" }
    }
  }

  # Example: Packetbeat processing
  if [@metadata][beat] == "packetbeat" {
    mutate {
      add_field => { "source_type" => "network" }
    }
  }
}

# ===================== OUTPUT =====================
output {
  elasticsearch {
    hosts => ["https://elasticsearch.company.com:9200"]
    user => "elastic"
    password => "YourElasticPassword"
    index => "%{[@metadata][beat]}-%{+YYYY.MM.dd}"
    ssl => true
    cacert => "/etc/logstash/certs/ca.crt"        # CA certificate for SSL verification
    ssl_certificate_verification => true
  }

  # Optional stdout for debugging
  stdout { codec => rubydebug }
}
```







