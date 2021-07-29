from netaddr import *

#Private Networks https://datatracker.ietf.org/doc/html/rfc1918
RFC1918_10 = IPNetwork('10.0.0.0/8')
RFC1918_172 = IPNetwork('172.16.0.0/12')
RFC1918_192 = IPNetwork('192.168.0.0/16')

#Test IP
ip = '172.25.25.100'

if IPAddress(ip) in ((IPNetwork(RFC1918_10))):
    print('Found', ip)
elif IPAddress(ip) in ((IPNetwork(RFC1918_172))):
    print('Found', ip)
elif IPAddress(ip) in ((IPNetwork(RFC1918_192))):
    print('Found', ip)
else:
    print(f'The Ip {ip} is out of range')

