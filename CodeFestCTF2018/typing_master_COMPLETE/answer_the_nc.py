#! /usr/bin/env python
from pwn import *
import re

r = remote('34.216.132.109', 9093)
question_str = r.recvline()
question = question_str.split(' ')
# print question
# print 
r.recvline()


############### my way ################
# mid = question.index('followed')
# a = question[mid-3][1]
# cnt_a = int(question[mid-2])
# b = question[mid+2][1]
# cnt_b = int(question[mid+3])
# reply = a*cnt_a + b*cnt_b +str(ord(a) + ord(b))
# # print reply
# r.sendline(reply)
# print r.recvline().split()[-1]

############ way with re ############
numbers = re.findall(r"'(\w)' (\d+)", question_str)
string = []
# print numbers
string.append(numbers[0][0] * int(numbers[0][1]))
string.append(numbers[1][0] * int(numbers[1][1]))
string.append(str(ord(numbers[0][0])+ord(numbers[1][0])))
ans = ''.join(string)
# print ans
r.sendline(ans)
print r.recvline().split()[-1]
r.close()














