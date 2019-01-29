#! /usr/bin/env python

from pwn import *

c = open('ciphertext.txt', 'rb')
content = c.readline()
# print content
after_b64d = b64d(content)
# print after_b64d
for key in range(256):
	tried = xor(key, after_b64d)
	if 'flag{' in tried:
		print tried
		break

# print 'end of program'



