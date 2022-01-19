# IMPORTS
from ipaddress import IPv4Network
from ipaddress import IPv4Address


# VERIABLES - PRIVATES NETWORKS https://datatracker.ietf.org/doc/html/rfc1918
RFC1918_10 = IPv4Network('10.0.0.0/8')
RFC1918_172 = IPv4Network('172.16.0.0/12')
RFC1918_192 = IPv4Network('192.168.0.0/16')

# TEST IP
ip = '10.140.140.2'

#LOOP CHECK
if IPv4Address(ip) in ((IPv4Network(RFC1918_10))):
        print('Class C found', ip)
elif IPv4Address(ip) in ((IPv4Network(RFC1918_172))):
        print('Class B found', ip)
elif IPv4Address(ip) in ((IPv4Network(RFC1918_192))):
        print('Class A found', ip)
else:
    print('Its not a internal IP')




