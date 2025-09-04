# Load Balancing

### Types of Load Balance:
1. Layer 4 Load Balance
   * TCP 
2. Layer 7 Load Balance
   * HTTP / HTTPS
   * Separate requests by URL address

### Load Balancing Algorithms:
* `roundrobin` : Send request sequential 1, 2, 3, ... (With weight)
* `static-rr` : Static roundrobin (Without weight)
* `leastconn` : Send request to server with less connections
* `first` : Send to the server which answer the signal first (Faster server)
* `hash` : Include source, uri, url_param(), hdr(), rdp-cookie
* `source` : Group clients in scopes with source address (Answer till the server went down) (Geo_IP)
* `uri` : Send request, related to the address form
* `url_param` : Send request, related to the parameters in the URL
* `hdr(<name>)` : Send request, related to headers the client used

### HaProxy Server Load Balancing Solutions:
1. `Active / Passive` : Using Floating IP (Set health check on HaProxy Servers)
2. `Active / Active` : Using DNS Records referred to HaProxy Servers (Set health check on DNS records) 
3. `Keepalived`




