# Kubernetes Concepts:

**1. Basic Structure**

* `Cluster` : A group of nodes working together to run containers.
* `Node` : A physical or virtual server that runs containers.
* `Control Plane Node` : Handles management and scheduling.
* `Worker Node` : Executes Pods.
* `Pod` : The smallest deployable unit that can contain one or more related containers.
* `Namespace` : Logical separation of resources for multi-project or multi-team environments.
* `Label and Selector` : Used for identifying, grouping, and filtering resources.

**2. Management and Interaction**

* `kubectl` : CLI tool for managing a Kubernetes cluster.
* `Context` : Settings for switching between multiple clusters.
* `Kubeconfig` : Configuration file storing connection, user, and context info.

**3. Core Objects**

* `Service` : Network abstraction that provides stable access to Pods.
* `ClusterIP` : Internal communication between services.
* `NodePort` : Exposes services on node ports for external access.
* `LoadBalancer` : Uses a cloud load balancer for public access.
* `Deployment` : Manages versioning, scaling, and rolling updates for Pods.
* `ReplicaSet` : Ensures a specified number of Pods are running.
* `StatefulSet` : For stateful applications like databases.
* `DaemonSet` : Ensures a Pod runs on every node (e.g., monitoring agents).
* `Job and CronJob` : For one-time or scheduled tasks.

**4. Storage and Configuration**

* `ConfigMap` : Stores non-sensitive configuration data.
* `Secret` : Stores sensitive data like passwords or API keys.
* `Volume` : Storage attached to a Pod.
* `PersistentVolume` (PV) and `PersistentVolumeClaim` (PVC) : Cluster-level persistent storage management.

**5. Security and Access**

* `RBAC (Role-Based Access Control)` : Manages permissions for users and services.
* `ServiceAccount` : Provides identity for Pods to securely interact with the API server.
* `NetworkPolicy` : Controls traffic between Pods.

**6. Monitoring and Troubleshooting**

* `Logs` : Inspect Pod logs using kubectl logs.
* `Events` : View cluster events for debugging.
* `Probes (Liveness, Readiness, Startup)` : Check container health and readiness.
* `Metrics` : Collect performance data with tools like Prometheus and Grafana.

**7. Advanced Concepts**

* `Ingress` : Manages HTTP/HTTPS access to services via controllers.
* `Helm` : A package manager for simplifying app deployment in Kubernetes.
* `Custom Resource Definition (CRD)` : Extends Kubernetes with custom resource types.
* `Operator` : Automates the management of complex applications or services.


## 🧱 Kubernetes Core Components:

**`pod` -> `Node` -> `Cluster`**

✅ 1. Control Plane Components:
> These components manage and control the entire cluster. They make global decisions and ensure the desired state is enforced.

* `kube-apiserver` : The central API server that exposes the Kubernetes API. All requests from users or components go through this.
* `etcd` : A distributed key-value store used as the backing store for all cluster data and state.
* `kube-scheduler` : Assigns newly created Pods to appropriate Nodes based on resource usage, affinity/anti-affinity rules, taints/toleration, etc.
* `kube-controller-manager` : Runs various controllers (Deployment, ReplicaSet, Job, etc.) to maintain cluster state.
* `cloud-controller-manager` : Integrates Kubernetes with cloud providers like AWS, GCP, Azure for provisioning load balancers, volumes, etc.

✅ 2. Node (Worker) Components:

> These components run on each node in the cluster and are responsible for running the actual containers.

* `kubelet` : Agent that runs on each node. Communicates with the control plane and ensures containers are running in Pods.
* `kube-proxy` : Maintains network rules and forwards traffic to the correct Pods across the cluster.
* `Container Runtime` : Software responsible for running containers (e.g., Docker, containerd, CRI-O).

🧩 Additional Kubernetes Concepts:

* `Pod` : The smallest deployable unit in Kubernetes. A Pod may contain one or more containers that share networking and storage.
* `Deployment` : Manages ReplicaSets and provides declarative updates to Pods (supports rolling updates, rollback, scaling).
* `ReplicaSet` : Ensures a specified number of Pod replicas are always running.
* `Service` : Exposes Pods as a network service with a stable IP and DNS name.
* `Namespace` : Logical isolation of Kubernetes resources. Useful for separating dev/stage/prod environments.
* `Ingress` : Manages external HTTP/HTTPS access to Services using routing rules. Acts like a reverse proxy.
* `ConfigMap / Secret` : Provides configuration data and sensitive information (like passwords, tokens) to Pods.
* `Volume / PersistentVolume (PV/PVC)` : Enables persistent storage for containers. Useful for databases, file systems, etc.
* `Job / CronJob` : Runs batch or scheduled tasks inside the cluster.

🧭 Simplified Architecture Diagram:
```sh
# Control Plane (Master):
├── kube-apiserver
├── etcd
├── kube-scheduler
├── controller-manager

# Worker Nodes:
├── kubelet
├── kube-proxy
├── container runtime
├── pods
```

### ✅ Key Takeaways:

- The `Control Plane` handles management and scheduling.
- `Worker Nodes` run the actual application workloads.
- `Pods` are the fundamental unit of deployment.
- Kubernetes follows a `declarative model` : you describe the desired state, and Kubernetes makes it happen.




