Setup up persistent iptables rules
==================================

This role will setup persistent ingress firewall based on iptables.

By default it will open:
  - communication on port 22 (SSH)
  - 

This role will set default INPUT policy to DROP and enable SSH access.
There are also 2 variables for DNS and NTP access.
Other rules are defined in `firewall_allow` list (default values are defined 
for Hetzner Infrastructure)
