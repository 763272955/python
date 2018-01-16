#-*- coding: utf-8 -*-
import  os
import sys
import numpy as np
import itertools

color = [u'红',u'绿', u'蓝', u'黄']
kill =[u'盾', u'枪', u'弩']
names = [u'理查德', u'席恩', u'吉利特', u'罗兰', u'莱奥', u'爱德华', u'贝奥武夫', u'伊撒尔']
data = []
number = {}
i=0
j=0
li = []
ai = []
yi = []
ji = []
bei = []
lai = []
xi = []
luo = []

for x in itertools.product(names, color, kill):
    # print 'x is \n',x
    data_ = ''.join(x)  #把
    data.append(data_)
num=len(data)
data=np.array(data)
for i in range(0,len(data),12):
    number[j] = data[i:i+12]
    j+=1


for k1 in itertools.product(number[0],number[1]):
    li_ = ''.join(k1)
    li.append(li_)
print li
for k2 in itertools.product(number[0],number[2]):
    li_ = ''.join(k2)
    li.append(li_)
for k3 in itertools.product(number[0],number[3]):
    li_ = ''.join(k3)
    li.append(li_)
for k4 in itertools.product(number[0],number[4]):
    li_ = ''.join(k4)
    li.append(li_)
for k5 in itertools.product(number[0],number[5]):
    li_ = ''.join(k5)
    li.append(li_)
for k6 in itertools.product(number[0],number[6]):
    li_ = ''.join(k6)
    li.append(li_)
for k7 in itertools.product(number[0],number[7]):
    li_ = ''.join(k7)
    li.append(li_)
for k7 in li:
    print  k7
for a1 in itertools.product(number[1],number[2]):
    ai_ = ''.join(a1)
    ai.append(li_)
for a2 in itertools.product(number[1],number[3]):
    ai_ = ''.join(a2)
    ai.append(li_)
for a3 in itertools.product(number[1],number[4]):
    ai_ = ''.join(a3)
    ai.append(li_)
for a4 in itertools.product(number[1],number[5]):
    ai_ = ''.join(a4)
    ai.append(li_)
for a5 in itertools.product(number[1],number[6]):
    ai_ = ''.join(a5)
    ai.append(li_)
for a6 in itertools.product(number[1],number[7]):
    ai_ = ''.join(a6)
    ai.append(li_)
for a6 in ai:
    print  a6
for l1 in itertools.product(number[2],number[3]):
    lai_ = ''.join(l1)
    lai.append(lai_)
for l2 in itertools.product(number[2],number[4]):
    lai_ = ''.join(l2)
    lai.append(lai_)
for l3 in itertools.product(number[2],number[5]):
    lai_ = ''.join(l3)
    lai.append(lai_)
for l4 in itertools.product(number[2],number[6]):
    lai_ = ''.join(l4)
    lai.append(lai_)
for l5 in itertools.product(number[2],number[7]):
    lai_ = ''.join(l5)
    lai.append(lai_)
for l5 in lai:
    print  l5
for y1 in itertools.product(number[3],number[4]):
    yi_ = ''.join(y1)
    yi.append(yi_)
for y2 in itertools.product(number[3],number[5]):
    yi_ = ''.join(y1)
    yi.append(yi_)
for y3 in itertools.product(number[3],number[6]):
    yi_ = ''.join(y3)
    yi.append(yi_)
for y4 in itertools.product(number[3],number[7]):
    yi_ = ''.join(y4)
    yi.append(yi_)
for y4 in yi:
    print  y4
for luo2 in itertools.product(number[4],number[5]):
    luo_ = ''.join(luo2)
    luo.append(luo_)
for luo1 in itertools.product(number[4],number[6]):
    luo_ = ''.join(luo1)
    luo.append(luo_)
for luo3 in itertools.product(number[4],number[7]):
    luo_ = ''.join(luo3)
    luo.append(luo_)
for luo3 in luo:
    print  luo3
for j1 in itertools.product(number[5],number[6]):
    ji_ = ''.join(j1)
    ji.append(ji_)
for j2 in itertools.product(number[5],number[7]):
    ji_ = ''.join(j2)
    ji.append(ji_)
for j2 in ji:
    print  j2
for i1 in itertools.product(number[6],number[7]):
    bei_ = ''.join(i1)
    bei.append(bei_)
for i1 in bei:
    print  i1


# for l in  file:
#     print l
# for x in data:
#     print x
#     if i == 11:
#         print '\n'
#         i+=1

def digui(i,j):
    ai = []
    for a1 in itertools.product(number[1], number[2]):
        ai_ = ''.join(a1)
        ai.append(li_)
    return ai






