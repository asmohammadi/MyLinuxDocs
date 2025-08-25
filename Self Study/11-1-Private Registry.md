# Private Registry

```sh
docker pull registry:2 # Download Registry image
```
```sh
# Create a container for registry:
docker run -d \
  -p 5000:5000 \
  --restart=always \
  --name registry \
  registry:2
```
```sh
# Save images in another Disk using volume:
docker run -d \
  -p 5000:5000 \
  --restart=always \
  --name registry \
  -v /opt/registry-data:/var/lib/registry \
  registry:2
```

```sh
# Local Registry Address:
http://localhost:5000
```

### Tag local images and push them:
```sh
docker pull nginx:latest
docker tag nginx:latest localhost:5000/mynginx
docker push localhost:5000/mynginx
```
```sh
# Pull images from Local Registry:
docker pull localhost:5000/mynginx
# or:
docker pull 192.168.1.10:5000/mynginx
```

### Insecure Registry:
> Local registry without SSL
> For using `Local Registry` without SSL need to create or edit json file in `/etc/docker/daemon.json`.

```sh
# Add this to daemon.json file:
{
  "insecure-registries" : ["localhost:5000"]
}
# Then:
systemctl restart docker
```

```sh
curl http://localhost:5000/v2/_catalog # Display images
curl http://localhost:5000/v2/mynginx/tags/list # Display tags
```

### Secure Private Registry:

```sh
# Add SSL to Registry:
docker run -d \
  -p 443:5000 \
  --restart=always \
  --name registry \
  -v /opt/registry-data:/var/lib/registry \
  -v /path/to/cert.pem:/certs/domain.crt \
  -v /path/to/key.pem:/certs/domain.key \
  -e REGISTRY_HTTP_ADDR=0.0.0.0:5000 \
  -e REGISTRY_HTTP_TLS_CERTIFICATE=/certs/domain.crt \
  -e REGISTRY_HTTP_TLS_KEY=/certs/domain.key \
  registry:2
```

### Basic Authentication for Registry:
```sh
# Install htpasswd:
apt install apache2-utils
# Create User File:
mkdir auth
htpasswd -Bc auth/htpasswd myuser
# Add more users:
htpasswd -B auth/htpasswd ali
```
* htpasswd path : `/home/user/registry/auth/htpasswd`
* htpasswd path : `/opt/registry/auth/htpasswd`
* htpasswd structure : `UserName:Hashed_Password`
* `-B` : Bcrypt secure Algorithm
* `-c` : Create file (Just first time)

```sh
# Registry with Authentication:
docker run -d \
  -p 5000:5000 \
  --restart=always \
  --name registry \
  -v /opt/registry-data:/var/lib/registry \
  -v $(pwd)/auth:/auth \
  -e "REGISTRY_AUTH=htpasswd" \
  -e "REGISTRY_AUTH_HTPASSWD_REALM=Registry Realm" \
  -e "REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd" \
  registry:2
```
```sh
# Login to registry:
docker login localhost:5000
```






