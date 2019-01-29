#! /usr/bin/env python
import requests
import re

host = 'http://34.216.132.109:8083'
first_page = '/fp/'

s = requests.Session()

content = s.get(host+first_page)

cnt = 1
while True:
	next_page = re.findall(r'action="(.*?)"', content.text)[0]
	content = s.get(host+next_page)
	print cnt
	print content.text

	cnt += 1
	if cnt>1010:	break


	# break
print 'end'
