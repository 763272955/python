# -*- coding:utf-8 -*-

import re

i = 0
j = 0

# str = '++++++++++[>++++++++>+++++>++++++++>+++++++>++++++++++>+++++>+++++++++>++++++++++++<<<<<<<<-]>+.>-.<+.>>>+.>+.<<<-.>>+++.>>>>+.<-.--.<<+++++++.>>>----.<+++.<<++.>>----.<<----.---------.>-.+++++++.>>+++.<<<++.<<<+.++++++++.>++++.>>--.<<+++.<--------.>>>>>>-.<<<<+++.>>>+.-.<+.'
str = '++++++++++++[>++++>+++++>++++++>+++++++>++++++++>+++++++++>++++++++++<<<<<<<-]>>>>+++.<-----.>---.<+++.>>>>+++.<<<<----.>>>++++++.<<<<<+++.--.>>>>>----.<<<++++.<<+++.>>>>+++.>---.>++.'
dict = {}
cout = ''

str_split = re.compile(r'(.*?)\[(.*?)\](.+)')
str_ = str_split.search(str).groups()
num_loop = len(str_[0])
for x in range(len(str_[1])):
    if str_[1][x] == '>':
        dict[i] = j
        i += 1
        j = 0
    if str_[1][x] == '+':
        j += 1
    if str_[1][x] == '<':
        dict[i] = j
del dict[0]
for x in range(1,len(dict)+1):
    dict[x] = (dict[x] * num_loop)
i = 0
for x in range(len(str_[2])):
    if str_[2][x] == '>':
        i += 1
        j = 0
    if str_[2][x] == '<':
        i -= 1
        j = 0
    if str_[2][x] == '+':
        j += 1
    if str_[2][x] == '-':
        j -= 1
    if str_[2][x] == '.':
        dict[i] += j
        cout += chr(dict[i])
        j = 0
print cout