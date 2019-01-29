from pwn import *
context.log_level="error"
import string
chars = string.ascii_lowercase + "_"
flag = ""    
for j in range(30):
    print "flag:",flag
    for i in chars:
        io = remote("crypto.chal.csaw.io",8040)
        print io.recv()
        io.sendline((i+flag)*20)
        print (i+flag)
        out = io.recvline()
        l = ord(out[-2])
        print "len=",l, i
        if l<35:                  #<== You have to edit this manually
            print i
            flag=i+flag
            break
        io.close()



