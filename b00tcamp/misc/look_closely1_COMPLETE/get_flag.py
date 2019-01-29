#! /usr/bin/env python

ll = [98, 48, 99, 116, 102, 123, 115, 51, 99, 114, 51, 116, 95, 65, 83, 67, 73, 73, 125]
new = []
for i in ll:
	new += chr(i),
print ''.join(new)
