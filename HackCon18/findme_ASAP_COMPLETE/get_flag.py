#! /usr/bin/env python

f = open('findme.txt', 'r')

data = f.read()
data2 = data.split(' ')

s = ''

for c in data2:
	if c=='':	continue
	s += chr(int(c))
ind = s.find('d4rk')

flag = ''
for i in range(ind, ind+100):
	if s[i]==' ':	break
	flag += s[i]

print flag


f.close()
