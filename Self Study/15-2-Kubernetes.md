# Kubernetes

## Install Minikube:
> Before installing Kubernetes the User must be member of `docker` Group.

```sh
sudo usermod -aG docker $USER
```
```sh
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
dpkg -i minikube_latest_amd64.deb
minikube version
```

### Install KubeCTL:

```sh
# Download KubeCTL file:
curl -LO https://dl.k8s.io/release/v1.30.1/bin/linux/amd64/kubectl
# Set permission:
chmod +x kubectl
# Move to System Path:
mv kubectl /usr/local/bin/
# Check installation:
kubectl version --client
```

## Running Minikube:
```sh
# Creating a VM on Docker & Installing Kubernetes on it:
minikube start --driver=docker
```
```sh
user1@server:~$ minikube start --driver=docker
* minikube v1.36.0 on Ubuntu 24.04
* Using the docker driver based on user configuration
* Using Docker driver with root privileges
* Starting "minikube" primary control-plane node in "minikube" cluster
* Pulling base image v0.0.47 ...
* Downloading Kubernetes v1.33.1 preload ...
    > preloaded-images-k8s-v18-v1...:  347.04 MiB / 347.04 MiB  100.00% 2.83 Mi
    > gcr.io/k8s-minikube/kicbase...:  502.26 MiB / 502.26 MiB  100.00% 2.85 Mi
* Creating docker container (CPUs=2, Memory=2200MB) ...
* Preparing Kubernetes v1.33.1 on Docker 28.1.1 ...
  - Generating certificates and keys ...
  - Booting up control plane ...
  - Configuring RBAC rules ...
* Configuring bridge CNI (Container Networking Interface) ...
* Verifying Kubernetes components...
  - Using image gcr.io/k8s-minikube/storage-provisioner:v5
* Enabled addons: storage-provisioner, default-storageclass

! /usr/local/bin/kubectl is version 1.30.1, which may have incompatibilities with Kubernetes 1.33.1.
  - Want kubectl v1.33.1? Try 'minikube kubectl -- get pods -A'
* Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

```sh
# Checking Kubernetes state:
kubectl cluster-info
kubectl get nodes
kubectl get pods -A
```

### Update KubeCTL version:
```sh
curl -LO https://dl.k8s.io/release/v1.33.1/bin/linux/amd64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

## Running a Test APP:
```sh
kubectl create deployment hello-nginx --image=nginx
kubectl expose deployment hello-nginx --type=NodePort --port=80
# Display Address:
minikube service hello-nginx --url
```

## Minikube / Cluster:
```sh
minikube status
minikube stop # Stop Minikube container but not remove it. (Turn Cluster Off)
minikube start # Start Minikube container again. (Turn Cluster On)
minikube delete # Delete Minikube container (Remove Cluster)
```

## Pod / Deployment / Services:
```sh
kubectl delete deployment hello-nginx # Remove deployment & all it's Pods
kubectl delete service hello-nginx # Remove Deployment & all Services
```

## Kubernetes Dashboard:
* `Kubernetes Dashboard` will run as a deployment & service.
* It will run in `kubernetes-dashboard` NameSpace.
* `Kubernetes Dashboard` by default using normal service account that has limited access. For Admin/Full access need to create a new service account & give the token to dashboard.

```sh
# Enable addon:
minikube addons enable dashboard
minikube dashboard # Run dashboard
minikube dashboard --url # Getting dashboard address

http://127.0.0.1:43879/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/
# It will run a browser with dashboard address & will using local proxy.
```













