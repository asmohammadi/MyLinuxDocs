# Log Management using SSL/TLS

## Using Self-signed SSL:
```sh
# Create Self-signed SSL on Log Server:
mkdir -p /etc/rsyslog-ssl
cd /etc/rsyslog-ssl

# Create Private Key:
openssl genrsa -out rsyslog-server.key 2048

# Create CSR (Certificate Signing Request)
openssl req -new -key rsyslog-server.key -out rsyslog-server.csr

# Create Self-Signed Certificate
openssl x509 -req -days 365 -in rsyslog-server.csr -signkey rsyslog-server.key -out rsyslog-server.crt

# Limit access on key:
chmod 600 rsyslog-server.key
```

### Configure Rsyslog with Self-signed SSL:
```sh
# /etc/rsyslog.conf or /etc/rsyslog.d/secure.conf
# Enable needed modules:
module(load="imtcp")
module(load="imudp")
module(load="imptcp")        # TCP
module(load="imtcp" StreamDriver.Name="gtls" StreamDriver.Mode="1" StreamDriver.AuthMode="anon")

# Certificates Path:
global(
    DefaultNetstreamDriver="gtls"
    DefaultNetstreamDriverCAFile="/etc/rsyslog-ssl/rsyslog-server.crt"
    DefaultNetstreamDriverCertFile="/etc/rsyslog-ssl/rsyslog-server.crt"
    DefaultNetstreamDriverKeyFile="/etc/rsyslog-ssl/rsyslog-server.key"
)

# Enable TLS Port:
input(type="imtcp" port="6514" StreamDriver.Name="gtls" StreamDriver.Mode="1" StreamDriver.AuthMode="anon")
```
```sh
systemctl restart rsyslog
```

### Configure Clients for using Self-signed SSL:
```sh
mkdir -p /etc/rsyslog-ssl
# Copy log server's certificate to client:
cp /etc/rsyslog-ssl/rsyslog-server.crt /etc/rsyslog-ssl/

# Edit file "/etc/rsyslog.conf" or "/etc/rsyslog.d/secure-client.conf"
module(load="omrelp")      # or omfwd for TCP/TLS

# Sending logs using TLS:
*.* action(
  type="omfwd"
  Target="Log-Server-IP"
  Port="6514"
  Protocol="tcp"
  StreamDriver="gtls"
  StreamDriverMode="1"
  StreamDriverAuthMode="anon"
  CAFile="/etc/rsyslog-ssl/rsyslog-server.crt"
)
```
```sh
systemctl restart rsyslog
```

## Using Real SSL:
```sh
# Certificate Path:
/etc/rsyslog-ssl/yourdomain.crt
/etc/rsyslog-ssl/yourdomain.key
/etc/rsyslog-ssl/ca-bundle.crt
```
```sh
# Limit access to certificate & Key:
chmod 600 /etc/rsyslog-ssl/yourdomain.key
```

### Rsyslog configuration using Real SSL:
```sh
# /etc/rsyslog.d/secure.conf or /etc/rsyslog.conf
# TLS Modules:
module(load="imtcp")
module(load="gtls")

# Certificate Path:
global(
    DefaultNetstreamDriver="gtls"
    DefaultNetstreamDriverCAFile="/etc/rsyslog-ssl/ca-bundle.crt"
    DefaultNetstreamDriverCertFile="/etc/rsyslog-ssl/yourdomain.crt"
    DefaultNetstreamDriverKeyFile="/etc/rsyslog-ssl/yourdomain.key"
)

# Enable TLS POrt:
input(
  type="imtcp"
  port="6514"
  StreamDriver="gtls"
  StreamDriverMode="1"
  StreamDriverAuthMode="x509/name"
)
```
```sh
systemctl restart rsyslog
```

### Client Configuration using Real SSL:
```sh
mkdir -p /etc/rsyslog-ssl
cp /etc/rsyslog-ssl/ca-bundle.crt /etc/rsyslog-ssl/

# Edit file "/etc/rsyslog.d/secure-client.conf":
module(load="omfwd")

*.* action(
  type="omfwd"
  Target="Log-Server-IP"
  Port="6514"
  Protocol="tcp"
  StreamDriver="gtls"
  StreamDriverMode="1"
  StreamDriverAuthMode="x509/name"
  CAFile="/etc/rsyslog-ssl/ca-bundle.crt"
)
```
```sh
systemctl restart rsyslog
```










