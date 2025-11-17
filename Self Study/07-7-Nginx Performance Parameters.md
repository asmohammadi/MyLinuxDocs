# Nginx Performance Parameters:

### Workers & Core settings:

```sh
worker_processes auto;

worker_connections 4096;
# Max connections per worker.
# Higher value = more simultaneous clients.

multi_accept on;
# Accept multiple new connections at once.
# Reduces accept overhead, improves performance under heavy traffic.

worker_rlimit_nofile 100000;
# Maximum open file descriptors.
# Prevents “too many open files” errors under high load.
```

### Events / Connections:
```sh
use epoll;
# Uses Linux epoll for event handling. 
# Most efficient event model for high-concurrency servers.

accept_mutex on;
# Prevent workers challenges for accept. 
# Reduce CPU overload.
```

### Buffer & Memory Optimization:

```sh
client_body_buffer_size 32k;
# Buffer size for client request body.
# Larger values reduce disk I/O.

client_header_buffer_size 4k;
# Buffer for request headers.
# Avoids “Request header too large” errors.

large_client_header_buffers 4 32k;
# Additional buffers for very large headers.
# Supports big cookies, JWTs, etc. Prevent "Bad request 400" in large headers.

output_buffers 2 64k;
# Buffers used for response generation.
# Larger buffers improve performance for dynamic output.
# Faster in delivering big answers.

postpone_output 1460;
# Delay sending partial responses.
# Reduces extra TCP packets → better performance.
```

### Gzip / Compression Optimization:
```sh
gzip on;
# Enable gzip compression.
# Reduces bandwidth usage + improves load time.

gzip_comp_level 4;
# Compression level (1–9).
# Higher = smaller files but more CPU usage.

gzip_min_length 1024;
# Minimum response size to compress.
# Avoids wasting CPU on tiny files.

gzip_types text/css application/json application/javascript;
# MIME types to compress.
# Ensures JS, CSS, HTML are compressed.

gzip_buffers
# Buffers used during gzip compression.
# Bigger files compress faster.
```

### Network & Socket Optimization:
```sh
keepalive_timeout 30;
# Duration to keep idle connections open.
# Lower = less memory usage; higher = fewer TCP handshakes.

keepalive_requests 1000;
# Max requests per keepalive connection.
# Higher values reduce connection overhead.

keepalive_disable
# Disable keepalive for specific user agents.
# Saves resources.

tcp_nopush on;
# Sends headers in one packet.
# Improves throughput for large files.

tcp_nodelay on;
# Sends small packets immediately.
# Reduces latency for small responses.

reset_timedout_connection on;
# Prevent using more RAM from abandoned connections.
```

### File System / Cache Performance:
```sh
sendfile
# Enables zero-copy kernel file transmission.
# Much faster static file serving.

open_file_cache max=50000 inactive=20s;
# Cache file descriptors, stats, and paths.
# Accelerates serving static files significantly.

open_file_cache_valid 30s;
# How often to check cache validity.
# Balances freshness vs. performance.

open_file_cache_min_uses 2;
# Minimum number of accesses before caching.
# Avoids caching rarely used files.

aio on;
# Enables async file I/O.
# Much faster static file delivery.

directio 4m;
# Bypasses OS cache for large files.
# Helps avoid memory pressure.

limit_conn
limit_req
# Throttling mechanisms.
# Protects server from overload.
```

### Upstream / Backend Performance:
```sh
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=mycache:100m max_size=1g;
# Defines cache zone.
# Determines cache size / efficiency.

proxy_cache_key "$scheme$request_method$host$request_uri";
# Cache optimization for API or Dynamic sites.

proxy_buffers 8 16k;
proxy_buffer_size 16k;
# Faster response for Reverse Proxy.
# Buffers for upstream responses.
# Larger values help dynamic sites.
# Prevents buffering to disk.

proxy_busy_buffers_size 64k;
# Buffers allowed to be “busy” sending.
# Helps with streaming content.

proxy_cache
# Enables caching for upstream responses.
# Huge performance boost for repeated requests.

proxy_connect_timeout 5s;
# Timeout for connecting to upstream.
# Lower values avoid hanging connections.

proxy_send_timeout 30;
proxy_read_timeout 30;
# Timeouts for upstream communication.
# Helps avoid stuck connections.

upstream backend {
    server 127.0.0.1:8080;
    keepalive 64;
}
# Reduce handshake between Nginx <-> backend.
```

### HTTP/2, TLS, and Modern Protocols:
```sh
ssl_session_cache shared:SSL:10m;
# Faster SSL handshake 

ssl_session_tickets on;
# Faster SSL handshake (If using SSL ticket)

ssl_buffer_size 4k;
# Size of SSL write buffer.
# Adjust for optimal CPU/memory usage.

http2_max_concurrent_streams
# Sets maximum HTTP/2 streams per connection.
# Higher values improve multiplexing.

http2_chunk_size
# Chunk size for HTTP/2 responses.
# Larger values improve throughput.

ssl_session_cache
# Cache TLS session parameters.
# Faster TLS handshake, less CPU use.

ssl_session_timeout 10m;
# Session cache expiration.
# Longer = more reused sessions → better performance.
```

### Logging Optimization:
```sh
access_log /var/log/nginx/access.log main buffer=32k flush=5s;
# Reduce writing on disk.
# Controls log verbosity.
# Lower verbosity improves CPU & disk usage.

access_log off
# Disable access logs.
# Reduces I/O load drastically (useful for high traffic).

access_log buffer
# Buffers log writes.
# Better performance than writing per request.
```

