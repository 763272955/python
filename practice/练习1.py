#-*- coding: utf-8 -*-
import numpy as np
import random

names = np.array(['Bob', 'joe', 'will','Bob', 'will', 'joe', 'joe'])
data = np.random.randn(7, 4)
print names
print data
print  names == 'Bob'
arr = np.empty((8, 4))
print 'arr is \n ', arr
for i in range(8):
    arr[i]=i
print arr

