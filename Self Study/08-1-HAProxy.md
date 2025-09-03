# HAProxy


### Scenario:
* 1 HaProxy Server
* 3 Web Servers
* HAProxy Server: Docker Container (CentOS)
  * Local Port: 80
  * Container port: 80
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
    errorfile 508 /etc/haproxy/errors/508.http
 
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
haproxy -f /etc/haproxy/haproxy.cfg # Run HAProxy Service
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






