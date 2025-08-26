# DockerFile Security:

1. Source limitation for containers
2. Limit running containers with Root
3. Management of logs and rotate
4. Isolation of containers


### 1. Source limitation for Containers:

**RAM Limitation:**
```sh
docker run -d --memory="512m" nginx # Just use 512Mb of RAM
```

**CPU Limitation:**
```sh
docker run -d --cpus="1.5" nginx # Just use 1.5 core of CPU
```

**Swap Limitation:**
```sh
docker run -d --memory="512m" --memory-swap="1g" nginx # Maximum of RAM + 1Gb Swap
```

### 2. Limit running containers with Root:

**Simple way:**
```sh
docker run -d --user 1000:1000 nginx # Using User ID
```

**Using Dockerfile:**
```sh
FROM nginx
RUN addgroup -g 1001 mygroup && adduser -u 1001 -G mygroup -D myuser
USER myuser
```

### 3. Management of logs and rotate:

```sh
docker logs Container
```
```sh
# Enable Log Rotation:
docker run -d \
  --log-driver json-file \
  --log-opt max-size=10m \
  --log-opt max-file=3 \
  nginx
# Maximum 3 log files & each file 10Mb size in Json format
```

### 4. Isolation of containers:

**Network Limitation:**
```sh
docker run -d --network none nginx
```

**Limitation of linux capability:**
```sh
docker run -d --cap-drop ALL nginx # Removing all kernel capabilities
docker run -d --cap-add NET_BIND_SERVICE # Keep some of them
```

**Read-only Container:**
```sh
docker run -d --read-only nginx
```

```sh
# Complex Example:
docker run -d \
  --name secure-nginx \
  --memory="256m" \
  --cpus="0.5" \
  --user 1000:1000 \
  --read-only \
  --log-driver json-file \
  --log-opt max-size=5m \
  --log-opt max-file=2 \
  nginx
```

**Checking Container Security:**
```sh
docker inspect secure-nginx
```









