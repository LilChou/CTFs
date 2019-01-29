#! /usr/bin/env python
import random
from pwn import *

host = '34.216.132.109'
port = 9094

user = 'admin'


s = remote(host, port)
s.recv()
s.sendline(user)
s.recv()
s.sendline(str(1337))

# count_ = user_functions.generateID(user)%1000	#User ID/ UID in the table is always positive
for count_ in range(1000):
	print s.recv()
	random.seed("xorshift")
	count = 0;

	for ch in user:
		ra = random.randint(1, ord(ch))
		rb = (ord(ch) * random.randint(1, len(user))) ^ random.randint(1, ord(ch))

		count += (ra + rb)/2


	code = 1

	for i in range(1,count+count_):
		code = (code + random.randint(1, i) ) % 1000000

	final = random.randint(1,9) * 1000000 + code
	
	print count_, final

	s.sendline(str(final))


s.close()