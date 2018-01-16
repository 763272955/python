
# encoding: utf-8
import time
key = [
    10413,
    11676,
    9438,
    10608,
    15115,
    12772,
    12771,
    9042,
    2597,
    2716,
    2509,
    3150,
    2713,
    2606,
    2607,
    2306,
    2403,
    15636]
flag = raw_input('Please input the flag:')
index = 0
for i in flag:
    time.sleep(0.1)
    if not ord(i) * ord(i) ^ ord(i) % (31 + index) == key[index]:
        print 'Wrong answer!'
        quit()
        continue
    index += 1

if index == len(key):
    print 'You got it!'
else:
    print 'Wrong answer!'
