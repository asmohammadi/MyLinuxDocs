# Ansible

## Ansible:
> `Ansible` is an agentless automation & configuration management tool. `Ansible` connects to servers using SSH, and uses YAML-base Playbook to define automation tasks.

### 📦 Common Use Cases:
* Install and configure packages (Nginx, Docker, Firewall, etc)
* User management
* Run commands on multiple servers
* Manage files and permissions
* Automate backups and monitoring

## Installing Ansible:
```sh
# 1. Installing prerequisites:
apt update
apt install software-properties-common -y

# 2. Adding Ansible official repository:
add-apt-repository --yes --update ppa:ansible/ansible

# 3. Installing Ansible:
apt install ansible -y

# 4. Check installation:
ansible --version
```

## Ansible Inventory:
> An `Ansible Inventory` is a file or source that defines the list of target hosts (servers) on which Ansible commands, tasks, or playbooks will be executed.

It tells Ansible:
* What hosts to connect to
* How to connect to them (user, key, port)
* How to group them (e.g. web, db, prod, staging)
* What variables are associated with each group or host

### Types of Inventory:
* `Static Inventory` : A plain text file (usually .ini or .yaml) with hardcoded hostnames or IPs
* `Dynamic Inventory` : Inventory generated from external sources (e.g. AWS, GCP, scripts, plugins)

**Default inventory file path:** `/etc/ansible/hosts`

**New inventory path:**
```sh
mkdir ~/ansible-lab
cd ~/ansible-lab
nano inventory.ini
```

**Sample inventory content:**
```sh
[webservers]
192.168.56.101
192.168.56.102

[dbservers]
192.168.56.201

[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/id_rsa
```
**Test:**
```sh
ansible -i inventory.ini all -m ping
```
* `-i inventory.ini` : Inventory file path
* `all` : All Hosts & Groups
* `-m ping` : Ping module for testing SSH

**Test with LocalHost:**
```sh
# Add this to inventory:
[local]
127.0.0.1 ansible_connection=local
```
```sh
# Test:
ansible -i inventory.ini local -m ping
```

## Ansible.cfg:

> The `ansible.cfg` file is the main configuration file for Ansible. It defines how Ansible behaves by setting default values for options like:

* Inventory file location
* SSH timeout settings
* User privileges
* Log paths
* Connection methods
* and much more

📍 Where Ansible Looks for ansible.cfg (in order of precedence):
* ./ansible.cfg – In the current working directory
* Environment variable ANSIBLE_CONFIG – If set
* ~/.ansible.cfg – In the user’s home directory
* /etc/ansible/ansible.cfg – System-wide default

🟡 The first file found in this order is used, and others are ignored.

📝 Example of a basic ansible.cfg file:
```ini
[defaults]
inventory = inventory.ini
remote_user = admin_ssh
host_key_checking = False
retry_files_enabled = False
timeout = 60

[privilege_escalation]
become = True
become_method = sudo
become_user = root
```

🔎 Key Options Explained:
* `inventory` : Path to the inventory file
* `remote_user` : Default SSH user
* `host_key_checking` : Disables SSH fingerprint confirmation
* `retry_files_enabled` : Prevents creation of .retry files
* `timeout` : SSH connection timeout (in seconds)
* `become` : Enables privilege escalation (like sudo)
* `become_user` : User to switch to (typically root)

🎯 Using a local ansible.cfg:
* Keeps project configurations isolated
* Avoids repeating CLI options (-i, -u, etc.)
* Ensures consistent behavior across team members or scripts


