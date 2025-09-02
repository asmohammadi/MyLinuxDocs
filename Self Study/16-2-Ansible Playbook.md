# Ansible Playbook

## Ansible Playbook:
* An `Ansible Playbook` is a YAML file that defines a set of tasks to be executed on one or more remote systems.
* `Playbooks` are the core of Ansible’s automation model.
* They describe what to do, on which hosts, and how to do it — in a way that is human-readable, repeatable, and version-controllable.

### Structure of a Playbook:
A Playbook typically contains:
* `Hosts` — The target group of servers (from the inventory)
* `User Privileges` — Whether to run tasks with sudo (become)
* `Tasks` — The ordered list of actions to execute (install packages, copy files, start services, etc.)
* `Modules` — The actual logic (e.g. apt, yum, service, file, etc.)

## Sample Playbook: Install and Start Nginx LocalHost
```sh
# Create a Yaml file:
cd ~/ansible-lab
nano install-nginx.yml
```
```yaml
# install-nginx.yml:

- name: Install and start Nginx on localhost
  hosts: local
  become: true
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Ensure nginx is running
      service:
        name: nginx
        state: started
        enabled: yes
```
```sh
# Running Playbook:
ansible-playbook -i inventory.ini install-nginx.yml # With sudo permission
ansible-playbook -i inventory.ini install-nginx.yml --ask-become-pass # Without sudo permission
```

## Sample Playbook: Install and Start Nginx on remote server
1. Inventory:
```ini
[webservers]
192.168.100.10 ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/id_rsa
```
2. Playbook Yaml file:
```yaml
# install-nginx-remote.yml

- name: Install and start Nginx on remote server
  hosts: webservers
  become: true
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Ensure nginx is running and enabled
      service:
        name: nginx
        state: started
        enabled: yes
```

## Sample Playbook: Install and configuring a Web Server

**Scenario:**
* Create User
* Install Nginx
* Allow HTTP on Firewall
* Enable Firewall
* Copy custom file (index.html)
* Restart Nginx

**Project Structure:**
```sh
ansible-lab/
├── inventory.ini
├── ansible.cfg
├── setup-webserver.yml
└── files/
    └── index.html
```

```yaml
# Setup-WebServer.yml:

- name: Prepare a secure web server with user, firewall, and custom content
  hosts: webservers
  become: true

  vars:
    custom_user: webadmin

  tasks:
    - name: Create a new user
      user:
        name: "{{ custom_user }}"
        shell: /bin/bash
        state: present

    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes

    - name: Ensure UFW is installed
      apt:
        name: ufw
        state: present

    - name: Allow HTTP traffic in UFW
      ufw:
        rule: allow
        port: 80
        proto: tcp

    - name: Enable UFW (if not already enabled)
      ufw:
        state: enabled

    - name: Copy custom index.html
      copy:
        src: files/index.html
        dest: /var/www/html/index.html
        owner: "{{ custom_user }}"
        group: "{{ custom_user }}"
        mode: '0644'

    - name: Restart nginx
      service:
        name: nginx
        state: restarted
```








