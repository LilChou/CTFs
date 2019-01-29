#! /usr/bin/env python

import re

flag = []

f = open('secret.c', 'r')
content = [line[:-1] for line in f.readlines()]
f.close()
# print content
for line in content:
	# print line
	num = re.findall(r"(\s+)", line)
	if num:
		num = int(''.join(num).replace(' ','0').replace('\t', '1'), 2)
		if num in range(255):
			flag.append(chr(num))

print re.findall(r"CodefestCTF{.*}", ''.join(flag)[::-1])[0]