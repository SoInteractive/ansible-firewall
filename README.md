<p><img src="http://www.kvmtechnologia.hu/images/stories/firewall.jpg" alt="firewall logo" title="firewall" align="right" height="60" /></p>

Ansible Role: firewall
======================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-firewall.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-firewall) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.firewall-blue.svg)](https://galaxy.ansible.com/SoInteractive/firewall/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-firewall.svg)](https://github.com/SoInteractive/ansible-firewall/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Ansible role to setup persistent ingress firewall based on iptables with fail2ban.
By design it will open communication:
  - on loopback interface
  - on port 22 (SSH)
  - for NTP
  - for DNS

Requirements
------------

To run the role with fail2ban you need to install python-netaddr package.

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.firewall
```

Little more advanced usage (enable traffic on port 80 only for 10.0.0.0/8 subnet and 443 for everyone)
```yaml
- hosts: webserver
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

TODO
----

Refactor to enable idempotance tests
