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
print  'counts的长度是： ',len(time_zone)
def top_counts(count_dict, n=10):                                           #定义输出排名前十的区域并输出数值
    value_key_pairs = [ (count, kk) for kk, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
print top_counts(counts)
print 'conding is ',conding[0]['tz']
frame = DataFrame(conding)
print  'frame,tz[:10] is ',frame['tz'][:10]
tz_count = frame['tz'].value_counts()[:10]
print tz_count
print
clean_tz = frame['tz'].fillna('missing')    #把空值替换成unkown
clean_tz[clean_tz == ''] = 'unknown'
tz_counts = clean_tz.value_counts()
print tz_counts[:10]
# print 'tz_counts 10 is ', time_zone[:10]
print 'counts list is', counts.items()
# print 'tz_counts is ',
# plt.plot(tz_counts,tz_counts)
tz_counts[:10].plot(kind='barh', rot=0)
# plt.show()
print 'frame 1 is ', frame['a'][1]
print 'frame 50 is ', frame['a'][50]
print 'frame 51 is ', frame['a'][51]
# rest = Series([x.split()[0]for x in frame.a.dropna])
results = Series([x.split()[0]for x in frame.a.dropna()])
print results
print 'results8 is ',results.value_counts()[:8]
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'windows', 'not windows')
print 'operating 5 is ', operating_system[:10]
by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
print 'agg_counts10 is ', agg_counts[:10]
indexer = agg_counts.sum(1).argsort()
print 'indexer 5 is ',indexer[:5]
count_subset = agg_counts.take(indexer)[-10:]
print 'count_subset 10 is  \n', count_subset
normed_subset = count_subset.div(count_subset.sum(1),axis=0)  #归1作图
normed_subset.plot(kind='barh',stacked=True)
count_subset.plot(kind='barh',stacked=True)     #直接作图
plt.show()

