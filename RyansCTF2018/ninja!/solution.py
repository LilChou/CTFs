'''
we have to do something similar to port knock or port scan
and we found that the port on the server will close after a period
so it means we have to send something to it (as the challenge said)
and check the output.

The port: 10000, 31337, 4444, 31984
(need to be knocked in order)

the code is below

at our server:
> base64 solution.py | tr -d '\n'
 echo '<the base64 that above cmd generates>' | base64 -d > t.py
copy the above line

at the ctf server:
> <paste the entire line just copied>
> python t.py 10000
> python t.py 31337
> python t.py 4444
> python t.py 31984

and we saw the flag
'''

#! /usr/bin/env python

import socket
import sys
# HOST = 'google.com'	# The remote host
# PORT = 50007			# same host used as the server

def port_knock(port):
	host = '127.0.0.1'		# local host
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)

	try:
		s.connect((host, int(port)))
	except socket.error:
		print 'port is not open'
		return False

	try:
		s.send('Aye')
		data = s.recv(4096)
		data = 'Port '+str(port)+' is open. Received data: '+str(data)
	except socket.timeout:
		data = 'Port is open, but timeout'
	

	s.close()
	print data
	# return data
	return True

def scan():
	found_port = []
	for port in range(1,65535):
		connected = port_knock(port)
		if connected:	found_port += port,
	return found_port

# print scan()
port_knock(sys.argv[1] )


