ssh developer@10.10.20.161
open afd33f/n0/0
en
conf term
snmp-server community asdgas RO
end
copy run start
show snmp community
snmpget -v 1 -c asdgas [ipAddress] [OID]
snmpwalk -v2c -c asdgas [ipAddress]






