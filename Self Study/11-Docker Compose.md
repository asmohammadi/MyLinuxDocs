# Docker Compose

> `Docker Compose` is a tool for create & manage multiple containers which are connected with YAML file.


## Creating a YAML File:

> Creating `docker-compose.yml` file in `/multi-service/` path. 
```yml
# Simple example:
services:
  web:
    image: nginx
    ports:
      - "8080:80"
    volumes:
      - nginx_logs:/var/log/nginx
  
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: P@ssw0rd
    volumes: # Permanent data volume for DB
      - mysql_data:/var/lib/mysql
```

### Bridge Network:

> In `Bride` network, containers can connect to each other but by default have no connection to Host.
> We can use port-forward to connect to Host.

```yml
networks:
  custom-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.25.0.0/24 # IP range other than Host network

volumes:
  mysql_data:
  nginx_logs:

services:
  web:
    image: nginx
    container_name: web1
    hostname: web1.local
    ports: # Port forwarding with Host
      - "8080:80"
    networks:
      custom-net:
        ipv4_address: 172.25.0.10
    volumes: # Permanent data volume for Web
      - nginx_logs:/var/log/nginx

  db:
    image: mysql:5.7
    container_name: mysql1
    hostname: mysql1.local
    environment:
      MYSQL_ROOT_PASSWORD: pass123
    networks:
      custom-net:
        ipv4_address: 172.25.0.20
    volumes: # Permanent data volume for DB
      - mysql_data:/var/lib/mysql
```

### Host Network (NAT):

```yml
services:
  web:
    image: nginx
    container_name: web_host
    network_mode: host
```

### Docker Compose Commands:

```sh
# Management:
docker compose version
docker compose up # Foreground running(Exit with Ctrl + P + Q)
docker compose up -d # Run docker-compose all services
docker compose down # Stop & remove all services
docker compose restart # Restart all services
docker compose start/stop # Start/Stop all services
docker compose up -d Container # Run specific service
docker compose restart Container # Restart specific service
docker compose stop Container # Stop specific service
```
```sh
# Logging:
docker compose logs # All services logs
docker compose logs Container # Specific service log
docker compose logs -f # Realtime logs
docker compose ps # Display all containers status
docker compose top # Display all process of services
docker compose config # Display final config before running YML
docker compose version # Display compose & plugin version
```
```sh
docker compose exec web bash # Entering web service shell
docker compose exec db mysql -u root -p # Running mysql in db service
docker compose run web ls -al /usr/share/nginx/html # Running temp commands in new service
```
```sh
# Cleaning:
docker compose down --volumes # Remove all services + volumes
docker compose down --rmi all # Remove all services + images
docker compose down --remove-orphans # Remove all orphaned containers
```
```sh
# Running multiple YAML files:
docker compose -f docker-compose.yml -f docker-compose.override.yml up -d
```
```sh
# ِDifferent YAML file Name/Path:
docker compose up -d web -f ./path/myfile.yml
docker compose -f /home/asghar/projects/myapp/docker-compose.dev.yml up -d # Different Path
docker compose -f docker-compose.prod.yml up -d # Different Name
```

### Secure Docker-Compose Example:
```yml
volumes:
  nginx_logs:

networks:
  secure-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.30.0.0/24

services:
  web:
    image: nginx:latest
    container_name: secure-nginx
    hostname: nginx.local
    networks:
      secure-net:
        ipv4_address: 172.30.0.10
    ports:
      - "8080:80"
    volumes:
      - nginx_logs:/var/log/nginx
    deploy: # This section will use in Docker Swarm
      resources:
        limits:
          cpus: '0.5'
          memory: 256M
    logging:
      driver: "json-file"
      options:
        max-size: "5m"
        max-file: "2"
    read_only: true
    user: "1000:1000"
    restart: always
```

















