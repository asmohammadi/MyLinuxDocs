# Sample Private Registry

## Scenario:
* Local registry on port 5000
* Using real SSL
* Using basic authentication with multi users
* Saving data on Disk using volume
* Using Docker Compose

## Project Structure:
```sh
docker-registry/
├── docker-compose.yml
├── certs/
│   ├── domain.crt
│   └── domain.key
├── auth/
│   └── htpasswd
├── data/
```

### Create Users file:
```sh
mkdir -p ../auth
htpasswd -Bc ../auth/htpasswd asghar
htpasswd -B ../auth/htpasswd ali
```

### Docker Compose File:
```yml
services:
  registry:
    image: registry:2
    restart: always
    ports:
      - "443:5000"
    environment:
      REGISTRY_HTTP_ADDR: 0.0.0.0:5000
      REGISTRY_HTTP_TLS_CERTIFICATE: /certs/domain.crt
      REGISTRY_HTTP_TLS_KEY: /certs/domain.key
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: "Private Docker Registry"
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/htpasswd
    volumes:
      - ./data:/var/lib/registry
      - ./auth:/auth
      - ./certs:/certs
```

### Running Registry:
```sh
docker compose up -d
```

### Trust SSL in Client:
```sh
mkdir -p /etc/docker/certs.d/registry.example.com
cp certs/domain.crt /etc/docker/certs.d/registry.example.com/ca.crt
```






