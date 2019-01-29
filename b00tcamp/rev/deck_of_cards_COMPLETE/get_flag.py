#! /usr/bin/env python
import operator
f = open('lines.txt', 'r')
dic = {}
location = 0
while True:
	line = f.readline()
	if line=='':	break
	if line=='\n':	break
	l = line.split(' ')

	if l[4][-3:]=='cmp':	
		# print l[8]
		s = l[8].split(',')[1]
	#	print 'chr=',
	#	print s
	#	print chr(int(s, 16))
		dic[location] = chr(int(s, 16))
		# dic[chr(int(s, 16))] = location
	elif l[4][-3:]=='vzx':	
		# print l[8]
		s = l[8][-7:-2]
	#	print 'loc=',
	#	print s
	#	print int(s, 16)
		location = int(s, 16)
	
# print 'eof'
sort = sorted(dic.items(), key=operator.itemgetter(0))
# print dic
# print sort
ans = []
for t in sort:
	ans += t[1],
print ''.join(ans)
