# Ansible Playbook Sample for Docker

### Sample Playbook: Install and configuring a Secure Web Server on docker container:

**Scenario:**
* create a container for Nginx
* Create User for Nginx
* Install Nginx on container
* Allow HTTP HTTPS on Firewall
* Enable Firewall
* Copy SSL Files (.crt, .key)
* Configuring Nginx with SSL
* Redirect Port 80 to 443
* Restart Nginx

**Project Structure:**
```sh
ansible-lab/
├── inventory.ini
├── ansible.cfg
├── secure-webserver-with-custom-ssl.yml
├── files/
│   └── ssl/
│       ├── example.com.crt
│       └── example.com.key
└── templates/
    └── nginx_ssl.conf.j2
```

**Ansible Config File:**
```sh
# ansible.cfg
[defaults]
inventory = ./inventory.ini
remote_user = ansible
host_key_checking = False
```

**Ansible Inventory:**
```ini
# inventory.ini
[webservers]
web1 ansible_host=192.168.1.100 ansible_user=ansible ansible_password=YourPassword
```

**Ansible Playbook:**
```yaml
# secure-webserver-with-custom-ssl.yml
- name: Secure Nginx Webserver in Docker
  hosts: webservers
  become: true

  vars:
    container_name: secure_nginx
    nginx_user: nginx
    domain_name: example.com

  tasks:

    - name: Install required packages
      apt:
        name:
          - docker.io
          - python3-docker
          - ufw
        state: present
        update_cache: true

    - name: Ensure Docker service is running
      service:
        name: docker
        state: started
        enabled: true

    - name: Create Nginx container
      community.docker.docker_container:
        name: "{{ container_name }}"
        image: nginx:latest
        state: started
        restart_policy: always
        published_ports:
          - "80:80"
          - "443:443"

    - name: Create Nginx user inside container
      community.docker.docker_container_exec:
        container: "{{ container_name }}"
        command: useradd -m -s /bin/bash "{{ nginx_user }}"
      ignore_errors: true

    - name: Copy SSL certificate
      community.docker.docker_cp:
        src: "files/ssl/{{ domain_name }}.crt"
        dest: "/etc/ssl/certs/{{ domain_name }}.crt"
        container: "{{ container_name }}"

    - name: Copy SSL key
      community.docker.docker_cp:
        src: "files/ssl/{{ domain_name }}.key"
        dest: "/etc/ssl/private/{{ domain_name }}.key"
        container: "{{ container_name }}"

    - name: Deploy Nginx config with SSL
      template:
        src: templates/nginx_ssl.conf.j2
        dest: "/etc/nginx/conf.d/{{ domain_name }}.conf"
      delegate_to: "{{ inventory_hostname }}"
      notify: Restart Nginx

    - name: Allow HTTP and HTTPS on firewall
      ufw:
        rule: allow
        port: "{{ item }}"
        proto: tcp
      with_items:
        - 80
        - 443

    - name: Enable firewall
      ufw:
        state: enabled
        policy: allow

  handlers:
    - name: Restart Nginx
      community.docker.docker_container_exec:
        container: "{{ container_name }}"
        command: nginx -s reload
```

**Nginx Configuration Template:**
```sh
# templates/nginx_ssl.conf.j2
server {
    listen 80;
    server_name {{ domain_name }};
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name {{ domain_name }};

    ssl_certificate /etc/ssl/certs/{{ domain_name }}.crt;
    ssl_certificate_key /etc/ssl/private/{{ domain_name }}.key;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}
```


