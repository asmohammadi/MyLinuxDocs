# Ansible Scenario:

* Defining scenario
* Creating inventory file and ansible.cfg
* Differences between running command and using modules in ansible
* Start working with ansible command

### Scenario:
* 4 Servers:
  * Loadbalancer -> Nginx
  * APP1 -> Nginx, Wordpress, PHP fpm
  * APP2 -> Nginx, Wordpress, PHP fpm
  * DB -> MySQL
* DNS Records:
  * lb.sudoer.net
  * app1.sudoer.net
  * app2.sudoer.net
  * db.sudoer.net
* Access limitation to DB Server to only APP Servers
* Iptables configuration
* SSH configuration
* Using Variables

```sh
# Ansible Directory Structure:
ansible/
├── group_vars
│   ├── all
│   ├── app
│   ├── db
│   └── lb
├── host_vars
│   ├── lb.sudoer.net
│   ├── app1.sudoer.net
│   ├── app2.sudoer.net
│   └── db.sudoer.net
├── inventory
│   └── main.yml
├── log
│   └── ansible.log
├── playbooks
│   └── default.yml
├── roles
│   ├── default
│   │    └── tasks
│   │        └── main.yml
│   ├── iptables
│   ├── mysql
│   ├── nginx
│   ├── php
│   ├── pkg
│   ├── ssh
│   └── wordpress
└── ansible.cfg
```

### Inventory:
```yml
all:
  hosts:
    lb.sudoer.net:
    db.sudoer.net:
    app1.sudoer.net:
    app2.sudoer.net:

app:
  hosts:
    app1.sudoer.net:
    app2.sudoer.net:

db:
  hosts:
    db.sudoer.net:

lb:
  hosts:
    lb.sudoer.net:
```

### Ansible.cfg:
```sh
[defaults]
inventory      = ./inventory/main.yml
remote_tmp     = /tmp
forks          = 150
sudo_user      = root
remote_user		 = root
roles_path    = ./roles
host_key_checking = False
log_path = ./log/ansible.log

[privilege_escalation]
#become=True
#become_method=sudo
#become_user=root
#become_ask_pass=False

[ssh_connection]
scp_if_ssh = True
```

### Check Hosts Connectivity:
```sh
ansible -i inventory/mail.yml all -a 'grep -i "^NAME=" /etc/os-release'
ansible -i app -a 'grep -i "^NAME=" /etc/os-release'
ansible -i db -a 'grep -i "^NAME=" /etc/os-release'
ansible -i lb -a 'grep -i "^NAME=" /etc/os-release'
```
* `all` : Group from inventory file

### Role Example:
```yml
# ansible/roles/default/tasks/main.yml

- name: Install git
  apt:
    name: git
    state: present
    update_cache: yes
```
```yml
# ansible/roles/default/tasks/main.yml
# Loop: Install more packages
- name: Install packages
  apt:
    name: "{{ item }}"
    state: present
    update_cache: yes
  loop:
    - git
    - htop
```
```yml
# ansible/playbook/default.yml
# Install Using Shell: (Less detail)
- name: Install packages with Shell
  shell: |
    apt update; apt install git htop sysstat tcpdump
```
```yml
# ansible/playbook/default.yml
# Create Directory:
- name: Create directory
  file:
    state: directory
    path: "/tmp/test"
```

### Playbook Example:
```yml
# ansible/playbook/default.yml

- name: default actions on all hosts
  hosts: all
  roles:
    - default
```

```sh
ansible-playbook playbook/default.yml --check # Check before running
ansible-playbook playbook/default.yml --check --diff # Display changes
```

### Variables:
1. Using Shell
2. Using Roles
3. Using host_vars directory
> Priority: Shell -> Roles -> host_vars

#### 1. Using Shell:
```yml
# ansible/playbook/default.yml
# Using Shell:
- name: Echo variable to file
  shell: |
    echo {{ VARIABLE }} > /tmp/test/VARIABLE

- name: Print variable
  debug: 
    msg: "{{ VARIABLE }}"
```
```sh
ansible-playbook playbook/default.yml -e "VARIABLE=Test_CMD" # Set Variable in command
```

#### 2. Using Roles:
```yml
# ansible/roles/web/defaults/main.yml
# Variable using Roles:
VARIABLE="Var_Default_Role"
```
```sh
ansible-playbook playbook/default.yml
```

#### 3. Using host_vars:
> Priority: host_vars -> Specific group_vars -> all group_vars

```yml
# ansible/inventory/host_vars/app1.sudoer.net.yml
# Variable using host_vars: (Just for APP1 Server)
VARIABLE: "APP1 HOST VARS"
```
```sh
# Structure:
ansible/
├── inventory
│   ├── group_vars
│   │   ├── all
│   │   ├── app
│   │   ├── db
│   │   └── lb
│   ├── host_vars
│   │   ├── lb.sudoer.net
│   │   ├── db.sudoer.net
│   │   ├── app1.sudoer.net
│   │   └── app2.sudoer.net
│   └── main.yml
```




