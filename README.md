Setup up persistent iptables rules
==================================

Ansible role to setup persistent ingress firewall based on iptables.
By default it will open:
  - communication on port 22 (SSH)
  - NTP communication
  - DNS communication
  - docker0 bridge networking

Requirements
------------

Iptables must be installed on target server.
Role currently supports only Debian-based environments.

Examples
--------

Basic usage in a playbook:
```yaml
- hosts: 'servers'
  become: true
  roles:
    - firewall
```
Little more advanced usage 
(enable traffic on port 80 only for 10.0.0.0/8 subnet and 443 for everyone)
```yaml
- hosts: 'servers'
  become: true
  roles:
    - firewall
  vars:
    firewall_allow:
      - { source: "10.0.0.0/8", port: "80" }
      - { port: "443" }
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.


