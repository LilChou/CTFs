#! /usr/bin/env python

# docs.pwntools.com

from pwn import *

# different ways to start the process
p = process(['./program', 'arg_a', 'arg_b']) 
p = process('./program')
p = remote('ip', 31337)



p.sendline("your input")	# with new line
p.send('your input')		# without input
p.sendafter("\n", "your stuff")


p.recvline()
p.recvall()
p.recvuntil("???")
p.recv(timeout=1)		# second(s)
p.recv()


p.rev(64)



