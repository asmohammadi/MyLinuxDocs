# Zabbix Agent with Ansible:

## Scenario:
* Installing Zabbix Agent 2 on 5 hosts
* Zabbix Server: 192.168.10.50
* Zabbix Proxy: 192.168.10.51
* Hosts: srv-01 ... srv-05
* Agent Mode: Active

### Inventory:
```ini
[zabbix_agents]
srv-01
srv-02
srv-03
srv-04
srv-05

[all:vars]
ansible_user=ubuntu
```
### Ansible Playbook:
```yml
---
- name: Install Zabbix Agent2 on Ubuntu servers (Zabbix 7.0 + Active mode + Proxy)
  hosts: zabbix_agents
  become: true

  vars:
    zabbix_repo_base: "https://repo.zabbix.com/zabbix/7.0/ubuntu"
    zabbix_server_ip: "192.168.10.50"
    zabbix_proxy_ip: "192.168.10.51"

  tasks:

    - name: Download Zabbix 7.0 release package
      ansible.builtin.shell: |
        wget {{ zabbix_repo_base }}/pool/main/z/zabbix-release/zabbix-release_7.0-2+ubuntu{{ ansible_distribution_release }}_all.deb -O /tmp/zabbix.deb
      args:
        executable: /bin/bash

    - name: Install Zabbix repo .deb package
      ansible.builtin.apt:
        deb: /tmp/zabbix.deb

    - name: Update apt cache
      ansible.builtin.apt:
        update_cache: yes

    - name: Install Zabbix Agent2
      ansible.builtin.apt:
        name: zabbix-agent2
        state: present

    - name: Deploy customized Zabbix Agent2 config
      ansible.builtin.template:
        src: zabbix_agent2.conf.j2
        dest: /etc/zabbix/zabbix_agent2.conf
        owner: root
        group: root
        mode: "0644"

    - name: Enable and restart Zabbix Agent2
      ansible.builtin.systemd:
        name: zabbix-agent2
        enabled: true
        state: restarted
```

### Agent configuration Template:
```sh
### Zabbix Agent 2 Active Mode Configuration

Server={{ zabbix_server_ip }}
ServerActive={{ zabbix_proxy_ip }}
Hostname={{ inventory_hostname }}

AllowKey=system.run[*]

Include=/etc/zabbix/zabbix_agent2.d/*.conf
```

### Run Playbook:
```sh
ansible-playbook -i inventory/hosts.ini playbooks/install_zabbix_agent2.yml
```

