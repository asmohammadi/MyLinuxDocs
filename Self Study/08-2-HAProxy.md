# HAProxy

### HaProxy Configuration Sections:
* `global` : General settings
* `default` : Default settings using in Frontend & Backend
* `frontend` : Client -> HaProxy path
* `backend` : HaProxy -> Servers path
* `listen` : Combine both Frontend & Backend to one section

### Simple HaProxy Configuration:
```sh
    global
        daemon
        maxconn 256

    defaults
        mode http
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms

    frontend http-in
        bind *:80
        default_backend servers

    backend servers
        server server1 127.0.0.1:8000 maxconn 32
```
```sh
# A sample with listen section:
    global
        daemon
        maxconn 256

    defaults
        mode http
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms

    listen http-in
        bind *:80
        server server1 127.0.0.1:8000 maxconn 32
```
### Bind Examples in configuration:
```sh
listen http_proxy
    bind :80,:443
    bind 10.0.0.1:10080,10.0.0.1:10443
    bind /var/run/ssl-frontend.sock user root mode 600 accept-proxy

listen http_https_proxy
    bind :80
    bind :443 ssl crt /etc/haproxy/site.pem

listen http_https_proxy_explicit
    bind ipv6@:80
    bind ipv4@public_ssl:443 ssl crt /etc/haproxy/site.pem
    bind unix@ssl-frontend.sock user root mode 600 accept-proxy

listen external_bind_app1
    bind "fd@${FD_APP1}"

listen h3_quic_proxy
    bind quic4@10.0.0.1:8888 ssl crt /etc/mycrt
```


### Scenario:
* 1 HaProxy Server
* 3 Web Servers
* HAProxy Server: Docker Container (CentOS)
  * Local Port: 80
  * Container port: 80
  * HaProxy Dashboard port: 1936
  * Load balance method: Roundrobin
* Web Server 1: Docker Container (Nginx)
  * Local Port: 8081
  * Container port: 80
* Web Server 2: Docker Container (Nginx)
  * Local Port: 8082
  * Container port: 80
* Web Server 3: Docker Container (Nginx)
  * Local Port: 8083
  * Container port: 80

### Docker Compose for Containers:
```yml
# Docker compose for HaProxy:
version: '3.5'
services:
  web:
    image: haproxy
    container_name: haproxy
    ports:
      - "80:80"
      - "1936:1936"
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg
    networks:
      - default

networks:
    default:
      name: haproxy
```

```yml
# Docker compose for Web Servers:
version: '3.5'
services:
  web:
    image: nginx
    container_name: web1
    ports:
      - "8081:80"
    volumes:
      - ./1.conf:/etc/nginx/conf.d/1.conf
      - ./index.html:/usr/share/nginx/html/index.html
    environment:
      - NGINX_PORT=80
    command: /bin/bash -c "exec nginx -g 'daemon off;'"
    networks:
      - default

networks:
    default:
      name: haproxy
```

### HaProxy Configuration:
```sh
global
    log         /dev/log local0
    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    maxconn     4096
    user        haproxy
    group       haproxy
    daemon

    stats socket /var/lib/haproxy/stats
 
defaults
    mode                    http
    log                     global
    option                  httplog
    option                  dontlognull
    option http-server-close
    option forwardfor       except 127.0.0.0/8
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout http-keep-alive 10s
    timeout check           10s
    maxconn                 3000
    errorfile 400 /etc/haproxy/errors/400.http
    errorfile 403 /etc/haproxy/errors/403.http
    errorfile 408 /etc/haproxy/errors/408.http
    errorfile 500 /etc/haproxy/errors/500.http
    errorfile 502 /etc/haproxy/errors/502.http
    errorfile 503 /etc/haproxy/errors/503.http
    errorfile 504 /etc/haproxy/errors/504.http
 
frontend http_front
    bind *:80
    default_backend web_servers
 
backend web_servers
    balance roundrobin
    server web1 192.168.1.11:80 check
    server web2 192.168.1.12:80 check
    server web3 192.168.1.13:80 check
```

```sh
haproxy -c -- /etc/haproxy/haproxy.cfg # Check HaProxy configuration before running
haproxy -f /etc/haproxy/haproxy.cfg # Run HAProxy
```

### HAProxy Configuration Sample:
```sh
global
    maxconn     50000 # Maximum connection per second
    #log         /dev/log local0
    #user       haproxy
    #group      haproxy
    #stats socket /run/haproxy/admin.sock user haproxy group haproxy mode 660 level admin
    nbproc      2 # Number of processors
    nbthread    4 # Number of Threads
    cpu-map     1 0 # First process on first CPU
    cpu-map     2 1 # Second process on second CPU

defaults
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    log                     global
    mode                    http
    option                  httplog
    maxconn                 3000 # For each Frontend & Backend

# Using HaProxy Web UI Interface:
# Web URL : http://haproxy:1936/haproxy?stats
listen  stats 
    bind 0.0.0.0:1936
    mode         http
    log          global
    maxconn      10
    clitimeout   100s
    srvtimeout   100s
    contimeout   100s
    timeout queue    100s
    stats enable
    stats hide-version
    stats refresh 30s
    stats show-node
    stats auth admin:password
    stats uri /haproxy?stats

frontend www.test.com
    bind 0.0.0.1:80
    use_backend api if { path_beg /api/ } # Check URL & if begins with api send to api backend
    use_backend jpeg if { path_beg /jpeg/ } # Check URL & if begins with jpeg send to jpeg backend
    use_backend tools if { path_beg /tools/ } # Check URL & if begins with tools send to tools backend
    default_backend web

frontend www.net.com
    bind 0.0.0.2:80
    default_backend web

backend web
    balance roundrobin
    cookie SERVERUSED nocache
    option httpchk HEAD / # Using for health check
    default-server check maxconn 20 # This option will use for all 3 web servers
    server web1 192.168.1.11:80 check
    server web2 192.168.1.12:80 check
    server web3 192.168.1.13:80 check
```

```sh
global
    log         /dev/log local0
    chroot      /var/lib/haproxy
    stats socket /run/haproxy/admin.sock user haproxy group haproxy mode 660 level admin
    stats timeout 30s
    user       haproxy
    group      haproxy
    daemon

    # Default SSL materials location:
    ca-base /etc/ssl/certs
    crt-base /etc/ssl/private

defaults
    mode                    http
    log                     global
    option                  httplog
    option                  dontlognull
    timeout connect         5000
    timeout client          50000
    timeout server          50000

listen dashboard
    bind :8081
    stats uri /
    stats refresh 10s
    stats enable
    stats auth admin:password

frontend test_frontend
    bind :8080
    mode tcp
    option tcplog
    default_backend test_backend

backend test_backend
    mode tcp
    balance static-rr
    server web1 172.16.1.11:80
    server web2 172.16.1.12:80
```

### Example for Two Path & Two Web Servers:
```sh

frontend test_frontend
    bind :8080
    mode http
    acl is_blog_path path_beg /blog
    acl is_main_path path_beg /
    use_backend test_backend1 is_blog_path
    use_backend test_backend2 is_main_path

backend test_backend1
    mode http
    balance first
    server web1 172.16.1.11:80 check

backend test_backend2
    mode http
    balance first
    server web2 172.16.1.12:80 check
```







