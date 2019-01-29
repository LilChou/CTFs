#! /usr/bin/env python

from pwn import *

host = '40.76.33.15'
port = 55777

f = remote(host, port)

cnt = 0
while True:
	print '--'+f.read()+'--'
	q = f.read()
	print 'q=('+q+')'
	q = q.split('.')[-1]

	question = q[2:]

	print 'question: '+str(question)
	ans = eval(question[:-1])
	print 'ans: '+str(ans)
	f.sendline(str(ans))
	print '*********'
	# cnt += 1
	# if cnt ==20:	break


f.close()