# Docker File:

> `Docker File` is a text file with step by step commands for creating a custom image.
  * Installing packages
  * Copy Files
  * Running config commands
  * Setting an executable APP

### Create custom image:

**Scenario:**
* `Image` : Nginx
* Create custom index.html file in `/usr/share/nginx/html` 
* `Name` : mynginx:1.0

```sh
# Structure:
custom-nginx/
├── Dockerfile
└── index.html
```
```sh
# Index.html:
<!DOCTYPE html>
<html>
<head>
  <title>My Custom Nginx</title>
</head>
<body>
  <h1>Hello from My Custom Nginx!</h1>
</body>
</html>
```
```sh
# Docker File:
FROM nginx:latest

COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```
* `FROM` : Base Image
* `COPY` : Copy index.html file to container
* `EXPOSE` : Publish port
* `CMD` : Command for running with `docker run`
* `-g` : Running foreground
* `daemon off` : Keep Nginx alive

```sh
# Create Image:
# Run in /custom-nginx/ path:
docker build -t mynginx:1.0 .
# or
docker build -f MyDockerfile -t myimage:tag .
docker build -f ./docker/custom/Dockerfile -t myimage:1.0 .
```
```sh
# Run docker from custom image:
docker run -d -p 8085:80 --name mynginx1 mynginx:1.0
# or
docker build -f /home/user1/custom/Dockerfile -t myimage:1.0 /home/user1/custom/
```

### Advance Docker File Concepts:

#### Layer:
> Each line in Dockerfile is a `Layer`.
> Docker will cache each `layer` , so in next customization just changed sections will `rebuild`.
> `Layers` will create from top to end.

```sh
# Example:
FROM ubuntu:20.04      # Layer 1
RUN apt update         # Layer 2
RUN apt install curl   # Layer 3
COPY index.html /      # Layer 4

# If we change index.html just Layer 4 will rebuild.
```
> Put files with more changes(like project code) at the end of Dockerfile, so the previous layers will cache.
```sh
RUN apt update && apt install curl vim -y
```

#### Cache:
> Docker will use layers `cache`.
> If the content have no change, the layer will not rebuild.
```sh
docker build --no-cache -t myimage . # Disable cache
```

### Expose:
> `Expose` is just for documentation.
> Just announce that the container will publish on this port.
> If we need to have access from Host, need to run with `-p`.
```sh
EXPOSE 80
docker run -p 8080:80 myimage
```

#### CMD vs ENTRYPOINT:

> When using `CMD` in docker file, if using `docker run` without command it will use `CMD`. But if using `docker run` with any command it will run the command.
> When using `ENTRYPOINT` in docker file, no matter running `docker run` with or without command, it will use `ENTRYPOINT` at all. 

```sh
# CMD Example:
FROM ubuntu
CMD ["echo", "Hello from CMD"]
# Run without command:
docker run myimage
# Result:
Hello from CMD
# Run with command:
docker run myimage ls -l
# It will list files.
```
```sh
# ENTRYPOINT Example:
FROM ubuntu
ENTRYPOINT ["echo", "Hello from ENTRYPOINT"]
# Run without command:
docker run myimage
# Result:
Hello from ENTRYPOINT
# Run with command:
docker run myimage ls -l
# Result:
Hello from ENTRYPOINT ls -l
```



