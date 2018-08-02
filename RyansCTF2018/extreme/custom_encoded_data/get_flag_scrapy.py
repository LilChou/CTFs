#! /usr/bin/env python

from scapy.all import *
from pwn import *

packets = rdpcap('flag.pcap')
# print packets.show()
print packets[3].show()
# print packets[3][Raw].load

print [ord(i) for i in packets[3][Raw].load]


print [ord(i) for i in 'FLAG: ']



print ''.join([chr(ord(i)/2) for i in packets[3][Raw].load])
