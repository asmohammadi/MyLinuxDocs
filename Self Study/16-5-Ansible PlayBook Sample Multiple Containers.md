# Ansible Playbook Sample Multiple Containers

### Sample Playbook: Install and configuring a Secure Web Server on multiple containers:

**Project Structure:**
```sh
ansible-lab/
├── ansible.cfg
├── inventory.ini
├── secure-webserver-with-custom-ssl.yml
├── group_vars/
│   └── all.yml
├── files/
│   └── ssl/
│       ├── example.com.crt
│       └── example.com.key
└── templates/
    └── nginx_ssl.conf.j2
```

**Variables file:**
```sh
# group_vars/all.yml
containers:
  - name: nginx-secure
    image: nginx:latest
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - /srv/nginx/conf:/etc/nginx/conf.d
      - /srv/nginx/certs:/etc/ssl
      - /srv/nginx/html:/usr/share/nginx/html
    ssl_domain: example.com
    type: nginx

  - name: mysql-db
    image: mysql:8.0
    ports:
      - "3306:3306"
    volumes:
      - /srv/mysql/data:/var/lib/mysql
    env:
      MYSQL_ROOT_PASSWORD: StrongRootPass
      MYSQL_DATABASE: appdb
      MYSQL_USER: appuser
      MYSQL_PASSWORD: StrongUserPass
    type: mysql
```

**Ansible Playbook:**
```yaml
# secure-webserver-with-custom-ssl.yml
---
- name: Deploy multiple containers with SSL and config
  hosts: webservers
  become: true

  tasks:

    - name: Create host volumes for containers
      file:
        path: "{{ item }}"
        state: directory
        owner: root
        group: root
        mode: '0755'
      loop: >
        {{ containers | map(attribute='volumes') | flatten | map('regex_replace', ':.+', '') | list | unique }}

    - name: Start containers
      community.docker.docker_container:
        name: "{{ item.name }}"
        image: "{{ item.image }}"
        state: started
        restart_policy: always
        published_ports: "{{ item.ports | default([]) }}"
        volumes: "{{ item.volumes | default([]) }}"
        env: "{{ item.env | default({}) }}"
      loop: "{{ containers }}"

    - name: Copy SSL files (only for nginx containers)
      community.docker.docker_cp:
        src: "files/ssl/{{ item.ssl_domain }}.crt"
        dest: "/etc/ssl/certs/{{ item.ssl_domain }}.crt"
        container: "{{ item.name }}"
      loop: "{{ containers }}"
      when: item.type == "nginx"

    - name: Copy SSL key (only for nginx containers)
      community.docker.docker_cp:
        src: "files/ssl/{{ item.ssl_domain }}.key"
        dest: "/etc/ssl/private/{{ item.ssl_domain }}.key"
        container: "{{ item.name }}"
      loop: "{{ containers }}"
      when: item.type == "nginx"

    - name: Deploy Nginx config (only for nginx containers)
      template:
        src: templates/nginx_ssl.conf.j2
        dest: "/srv/nginx/conf/{{ item.ssl_domain }}.conf"
      loop: "{{ containers }}"
      when: item.type == "nginx"
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
        container: "nginx-secure"
        command: nginx -s reload
```

**Nginx Configuration Template:**
```sh
# templates/nginx_ssl.conf.j2
server {
    listen 80;
    server_name {{ ssl_domain }};
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name {{ ssl_domain }};

    ssl_certificate /etc/ssl/certs/{{ ssl_domain }}.crt;
    ssl_certificate_key /etc/ssl/private/{{ ssl_domain }}.key;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }
}
```

