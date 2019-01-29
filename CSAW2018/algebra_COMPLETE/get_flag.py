#! /usr/bin/bash

from pwn import *
import math

r = remote("misc.chal.csaw.io", 9002)
r.recvuntil("*"*82)
while True:
        r.recvline()
        data = r.recvline()
        print data
        st = [str(s) for s in data.split()]
        operator = st[1]
        num =  st[0]
        num2 = st[2]
        result = st[4]
        if num == "X":
                if(operator == "-"):
                        answer = int(result) + int(num2)
                elif(operator == "+"):
                        answer = int(result) - int(num2)
                elif(operator == "*"):
                        f = float(result) / float(num2)
                        print f
                        if type(f)==float and int(str(f).split(".")[1]) == 0:
                        	answer = int(f)
                        else:
                        	answer = f
                elif(operator == "/"):
                        answer = int(result) * int(num2)
        elif num2 == "X":
                if(operator == "-"):
                        answer = (int(result) - int(num))*-1
                elif(operator == "+"):
                        answer = int(result) - int(num)
                elif(operator == "*"):
                        f = float(result) / float(num)
                        print f
                        if type(f)==float and int(str(f).split(".")[1]) == 0:
                        	answer = int(f)
                        else:
                        	answer = f
                elif(operator == "/"):
                        answer = int(result) * int(num)
        else:

        	data2 = data.strip().split("=")[0]
        	proccess = data2.replace("X","{0}")
        	p_result = data.strip().split("=")[1].strip()
        	for i in range(1,100):
        		make = eval(proccess.format(i))
        		if int(make) == int(p_result):
        			answer = i
        			break
        print answer
        r.sendline(str(answer))
print r.recv()
r.close()



