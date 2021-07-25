from netaddr import *

#Redes Reservadas
RFC1918_10 = IPNetwork('10.0.0.0/8')
RFC1918_172 = IPNetwork('172.16.0.0/12')
RFC1918_192 = IPNetwork('192.168.0.0/16')

#ip de teste
ip = '172.25.25.0'

if IPAddress(ip) in ((IPNetwork(RFC1918_10))):
    print('encontrei', ip)
elif IPAddress(ip) in ((IPNetwork(RFC1918_172))):
    print('encontrei', ip)
elif IPAddress(ip) in ((IPNetwork(RFC1918_192))):
    print('encontrei', ip)
else:
    print(f'O IP {ip} esta fora do escopo')

