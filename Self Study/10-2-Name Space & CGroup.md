# Name Space & CGroup

### Namespace:
* `Namespace` is using for isolation of processes or a group of processes
* Container will imagine that it has its own operating system

**Important Namespaces:**
* `PID namespace` : Separates processes. Processes inside one container cannot see the processes of another container.
* `NET namespace` : Isolates networking. Each container has its own network interface, IP address, routing table, and firewall rules.
* `MNT namespace` : Separates mount points. Each container has its own filesystem view.
* `UTS namespace` : Separates hostname and domain name. Each container can have a different hostname.
* `IPC namespace` : Isolates inter-process communication (such as shared memory).
* `USER namespace` : Separates users and UIDs. For example, a container can have a root user inside, while on the host it maps to an unprivileged user.

### CGroup:
* `CGroups` are a Linux kernel feature that allows resource management for groups of processes.
* Controlling  CPU, memory, disk I/O, and network bandwidth a container or process group can use.

**Capabilities of CGroup:**
* `CPU limitation` : Restrict how many CPU cores or how much CPU time a container can consume.
* `Memory limitation` : Define a maximum RAM usage (e.g., 512 MB).
* `I/O control` : Limit disk read/write operations.
* `Network control` : Restrict network bandwidth usage.
* `Prioritization` : Allocate resources fairly or give higher priority to certain processes or containers.

> In Docker, CGroups ensure that each container uses only its allocated share of resources, preventing one container from exhausting the host system.

### Namespace Management:
```sh
# List Namespaces:
lsns
# Show namespace of specific process:
ls -l /proc/PID/ns/
ls -l /proc/1234/ns/
```
```sh
# Create & Isolate Namespaces:
unshare --net --pid --mount --uts --ipc --fork /bin/bash # New Shell with isolated namespaces
```
```sh
# Connect to a namespace:
nsenter --target 1234 --net # Connect to Net namespace with PID
```
```sh
# In Docker:
docker inspect --format '{{.State.Pid}}' mycontainer
ls -l /proc/<PID>/ns/
```

### CGroup Management:
```sh
# Display CGroups:
cat /proc/self/cgroup
# Display CGroup's resources:
ls /sys/fs/cgroup/
```
```sh
# Create CGroup V1:
# Create New Group:
mkdir /sys/fs/cgroup/memory/test

# Set Memory limit to 100 MB:
echo 104857600 | sudo tee /sys/fs/cgroup/memory/test/memory.limit_in_bytes

# Adding PID of a process to the Group:
echo <PID> | sudo tee /sys/fs/cgroup/memory/test/cgroup.procs
```
```sh
# Create CGroup V2: (Newer)
# Create new CGroup:
mkdir /sys/fs/cgroup/mygroup

# Limit CPU to 20%:
echo "20000 100000" | sudo tee /sys/fs/cgroup/mygroup/cpu.max

# Adding PID to the Group:
echo <PID> | sudo tee /sys/fs/cgroup/mygroup/cgroup.procs
```

### Namespace & CGroup Management with SystemD:
```sh
# Memory limitation on a service:
systemctl set-property nginx.service MemoryMax=500M
systemctl set-property nginx.service CPUQuota=50%
```

### Namespace & CGroup Management in Docker:
```sh
# Memory limitation:
docker run -m 512m --memory-swap 1g ubuntu

# CPU limitation:
docker run --cpus="2" ubuntu

# Resource management:
docker inspect <container_id> | grep -i cgroup
```



