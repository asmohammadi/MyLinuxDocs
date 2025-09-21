# Ansible Structure - Best Practice

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






