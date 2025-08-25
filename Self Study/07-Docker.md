# Docker

### Installing Docker on Ubuntu 24.04:

```sh
# 1. Update
apt update && sudo apt upgrade -y

# 2. Installing prerequisites:
apt install ca-certificates # A Package of Trusted Certificates for connecting to Docker Repositories
apt install curl # For getting GPG Key
apt install gnupg # For managing signing keys
apt install lsb-release # To specify the Linux OS version 

# 3. Adding Docker Official GPG Key:
mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# 4. AddingDocker Official Repository (for Ubuntu 24.04 Noble):
echo \
"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
https://download.docker.com/linux/ubuntu noble stable" | \
tee /etc/apt/sources.list.d/docker.list > /dev/null

# 5. Update Repository List & Installing Docker:
apt update
apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# 6. Check installing version:
docker --version

# Check Docker Service:
systemctl status docker
```

#### Use Docker without Sudo:
```sh
sudo usermod -aG docker $USER # Add current User to docker Group
# Need to Logout & Login
```

### Container vs Image in Docker:

📦 What is a Docker Image?
- A Docker Image is a read-only template used to create containers.
- It contains everything needed to run an application: OS libraries, source code, configurations, and dependencies.
- Think of it as a snapshot or a blueprint.

✅ Example:
The official nginx image includes a minimal OS and the Nginx web server pre-installed.

🧱 What is a Docker Container?
- A Container is a running instance of an image.
- It runs in isolation from the host system and other containers.
- Containers share the host’s Linux kernel, which makes them lightweight and fast.

✅ Example:
You can create a running Nginx server from the nginx image and map it to port 8080.

🔄 Image vs. Container
* `Image`     : A read-only template used to create containers
* `Container` : A live, writable instance of an image

> You can run multiple containers from the same image.

💡 Key Characteristics
- You can launch multiple containers from a single image.
- Containers are isolated by default, but they can communicate over custom Docker networks.
- They are much lighter than virtual machines, as they don't include an OS kernel.

### Running first Container:

```bash
# Create & Run Nginx Container:
docker run -d -p HostPort:ContainerPort --name ContainerName ImageName
docker run -d -p 8080:80 --name web1 nginx
```
* `-d` : Background run
* `-p` : Port
* `--name` : Container Name
* `nginx` : Image Name

```bash
docker search ImageName # Search images
docker pull Image # Download Image from Docker Hub
docker push # Upload Image to Docker Hub
docker images # List images
docker images -a # List all images
docker ps # List containers
docker ps -a # List all containers
docker exec -it Container bash # Enter container Shell environment
    apt update && apt install nano -y # Execute command in container shell
docker logs Container # Display container log
docker inspect Container/Image # Display details of a container/image
docker stop/start Container
docker create --name ContainerName ImageName
docker rm Container # Remove container
docker container prune # Remove all stopped containers
docker rmi nginx # Remove Image
docker build -t mynginx:1.0 . # Create image from a docker file.
docker system prune -a # Remove all unused containers & images.
docker volume ls # Display all volumes

```

### Container FileSystem & Volume (Persistency):

> `/var/lib/docker/overlay2/` : Default path for temporary system files of running container.

#### Volume:
> `Volume` is used for saving persistent data.

```bash
docker volume create mydata # Create volume
docker run -d --name testvol -v mydata:/data busybox sleep 9999 # Connect volume to container
```

**Bind Mount:**
```bash
# Example:
mkdir /home/user1/Nginx-App
echo "From Host" > /home/user1/Nginx-App/host.txt

docker run -it --rm -v /home/user1/Nginx-App:/data busybox sh
cat /data/host.txt
```

