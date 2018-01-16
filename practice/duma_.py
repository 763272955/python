#-*- coding: utf-8 -*-

import itertools
import openpyxl

color = [u'红',u'绿', u'蓝', u'黄']
kill =[u'盾', u'枪', u'弩']
names = [u'理查德', u'席恩', u'吉利特', u'罗兰', u'莱奥', u'爱德华', u'贝奥武夫', u'伊撒尔']

dic = {}

for name in names:
    data = []
    for iter in itertools.product(color, kill):
        data_ = ''.join(iter)
        data_ += name
        data.append(data_)
        dic[name] = data
for x in range(len(names)):
    first = dic[names[x]]
    for y in range(x+1, len(names)):
        second = dic[names[y]]
        for iter in itertools.product(first,second):

            print 'vs'.join(iter),'胜利者是: \n'