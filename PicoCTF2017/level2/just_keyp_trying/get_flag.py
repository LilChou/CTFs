#! /usr/bin/env python
from scapy.all import *


mapping = {
	'0x0':"",
	'0x4':"a",
	'0x5':"b",
	'0x6':"c",
	'0x7':"d",
	'0x8':"e",
	'0x9':"f",
	'0xa':"g",
	'0xb':"h",
	'0xc':"i",
	'0xd':"j",
	'0xe':"k",
	'0xf':"l",
	'0x10':"m",
	'0x11':"n",
	'0x12':"o",
	'0x13':"p",
	'0x14':"q",
	'0x15':"r",
	'0x16':"s",
	'0x17':"t",
	'0x18':"u",
	'0x19':"v",
	'0x1a':"w",
	'0x1b':"x",
	'0x1c':"y",
	'0x1d':"z",
	'0x1e':"1",
	'0x1f':"2",
	'0x20':"3",
	'0x21':"4",
	'0x22':"5",
	'0x23':"6",
	'0x24':"7",
	'0x25':"8",
	'0x26':"9",
	'0x27':"0",
	'0x2f':"[",
	'0x30':']',
	'0x2d':'_',
 }
'''	
extract flag from data.pcap
from hint: http://www.usb.org/developers/hidpage/Hut1_12v2.pdf
we found out that this is a keyboard typein flag
'''
packets = rdpcap('data.pcap')


# print packets.show()
# print '--'
# print packets[0].show()
# print '--'
# print hex(packets[0][0].load[0])
# print mapping[0x9]
# print mapping[0x4]


for packet in packets:
	byte = hex(ord(packet[0].load[-6]))
	print mapping[hex(ord(packet[0].load[-6]))]
