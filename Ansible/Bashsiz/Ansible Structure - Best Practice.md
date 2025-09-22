# Ansible Structure - Best Practice

### Files Structure:
```sh
ansible-lab/
├── ansible.cfg
├── inventory.ini
├── playbook.yml
├── group_vars/
│   └── main.yml
├── host_vars/
│   └── main.yml
└── roles/
    └── tasks/
    │   ├── main.yml
    │   └── anything.yml
    └── vars/
    │   ├── main.yml
    │   └── anything.yml
    └── defaults/
    │   ├── main.yml
    │   └── anything.yml
    └── handlers/
    │   ├── main.yml
    │   └── anything.yml
    └── templates/
    │   ├── app1.cong
    │   └── app2.conf
    └── files/
        └── ssl/
        │   ├── ca.crt
        │   └── private.key
        └── dir/
            └── file
```

### Inventory Structure:
* `inventory.ini`
* `inventory.yml`

```sh
# Inventory Files Structure:
ansible/
└── inventory/
    └── reg-w/
    │   ├── hosts-datacenter1.ini
    │   └── hosts-datacenter3.ini
    └── reg-e/
    │   ├── hosts-datacenter2.ini
    │   └── hosts-datacenter4.ini
```
```sh
# inventory.ini
[all]
host1
host2
host3
host4
host5

[ssh]
web
app

[firewall:children]
web
db

[web]
host1
host2

[db]
host3
host4

[app]
host5
```
```yml
# inventory.yml
all:
  hosts:
    host1:
    host2:
    host3:
    host4:
    host5:

web:
  hosts:
    host1:
    host2:

db:
  hosts:
    host3:
    host4:

app:
  hosts:
    host5:
```








