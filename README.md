Setup up persistent iptables of firewalld rules
===============================================

This role will set default INPUT policy to DROP and enable SSH access.
There are also 2 variables for DNS and NTP access.
Other rules are defined in `firewall_allow` list (default values are defined 
for Hetzner Infrastructure)