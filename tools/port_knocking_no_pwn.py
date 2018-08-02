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
