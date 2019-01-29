#! /usr/bin/env python

f1 = open('file1').read()
f2 = open('file2').read()

flag = []
for i in range(len(f1)):
	if f1[i] == f2[i]:
		flag.append(f1[i])


print ''.join(flag)