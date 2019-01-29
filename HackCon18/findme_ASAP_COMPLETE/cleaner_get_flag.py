#! /usr/bin/env python

import re

f = open('findme.txt', 'r')

content = f.read()

print re.findall('d4rk{.*}c0de', ''.join([chr(int(x)) for x in content.split()]))[0] 

f.close()
