#-*- coding: utf-8 -*-
import json
import openpyxl
from pandas import DataFrame, Series
import pandas as pd; import numpy as  np
import matplotlib.pyplot as plt
from pylab import *
path = 'C:\Users\cuipeng0207\Desktop\example.txt'
# print open(path).readline()
conding = [json.loads(line) for line in open(path)]
print 'conding[0][''] is ', conding[0]['tz']
time_zone =[rec['tz'] for rec in conding if 'tz' in rec]
print 'time_zone[10]is ',time_zone[:10]
# sequence=time_zone[:10]
def get_counts(sequence):                           #定义计数项
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts
counts = get_counts(time_zone)
print 'counts is ',counts
def top_counts(count_dict, n=10):                                           #定义输出排名前十的区域并输出数值
    value_key_pairs = [ (count, kk) for kk, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
frame = DataFrame(conding)
results = Series([x.split()[0]for x in frame.a.dropna()])
print results
