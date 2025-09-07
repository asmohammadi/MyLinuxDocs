# Ansible Playbook Sample

## Sample Playbook: Install and configuring a Secure Web Server remotely:

**Scenario:**
* Create User
* Install Nginx
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
```ini
[webservers]
192.168.100.10 ansible_user=admin_ssh ansible_ssh_private_key_file=~/.ssh/id_rsa
```
```yaml
# Secure-WebServer-With-Custom-SSL.yml:

- name: Setup nginx with purchased SSL and redirect HTTP to HTTPS
  hosts: webservers
  become: true

  vars:
    custom_user: webadmin
    domain_name: example.com
    ssl_cert_local_path: files/ssl/example.com.crt
    ssl_key_local_path: files/ssl/example.com.key
    ssl_cert_remote_path: /etc/ssl/certs/example.com.crt
    ssl_key_remote_path: /etc/ssl/private/example.com.key

  tasks:
    - name: Create user
      user:
        name: "{{ custom_user }}"
        shell: /bin/bash
        state: present

    - name: Install nginx and ufw
      apt:
        name: "{{ item }}"
        state: present
        update_cache: yes
      loop:
        - nginx
        - ufw

    - name: Allow HTTP and HTTPS ports in firewall
      ufw:
        rule: allow
        port: "{{ item }}"
        proto: tcp
      loop:
        - 80
        - 443

    - name: Enable UFW
      ufw:
        state: enabled

    - name: Copy SSL certificate
      copy:
        src: "{{ ssl_cert_local_path }}"
        dest: "{{ ssl_cert_remote_path }}"
        owner: root
        group: root
        mode: '0644'

    - name: Copy SSL private key
      copy:
        src: "{{ ssl_key_local_path }}"
        dest: "{{ ssl_key_remote_path }}"
        owner: root
        group: root
        mode: '0600'

    - name: Configure nginx for SSL and redirect HTTP to HTTPS
      template:
        src: templates/nginx_ssl.conf.j2
        dest: /etc/nginx/sites-available/{{ domain_name }}
      notify:
        - Reload nginx

    - name: Enable nginx site
      file:
        src: /etc/nginx/sites-available/{{ domain_name }}
        dest: /etc/nginx/sites-enabled/{{ domain_name }}
        state: link
        force: yes

    - name: Remove default nginx site
      file:
        path: /etc/nginx/sites-enabled/default
        state: absent

    - name: Ensure nginx is running
      service:
        name: nginx
        state: started
        enabled: yes

  handlers:
    - name: Reload nginx
      service:
        name: nginx
        state: reloaded
```

```sh
# Nginx Configuration (Jinja2):
# templates/nginx_ssl.conf.j2
server {
    listen 80;
    server_name {{ domain_name }};
    return 301 https://$host$request_uri; # Redirect HTTP to HTTPS
}

server {
    listen 443 ssl;
    server_name {{ domain_name }};

    ssl_certificate {{ ssl_cert_remote_path }};
    ssl_certificate_key {{ ssl_key_remote_path }};

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        root /var/www/html;
        index index.html;
    }
}
```


