#-*- coding: utf-8 -*-
import colorsys
import itertools
import openpyxl
import argparse
import os
from collections import *
import urllib
import BeautifulSoup
import decimal
import contextlib
import thread
import threading
import time
import random
import numpy as np

#反向遍历
colors = ['red','green','blue','yellow','bin','red']
names = ['raymond','rache','matthew']
# for i in range(len(colors)-1,-1,-1):
#     print colors[i]
#高效
# for color in reversed(colors):
#     print color
#范围算数
# for i in xrange(6):
#     print i**2
#遍历列表下表及其值
# for i in xrange(len(colors)):
#     print i,'---->',colors[i]
#高效
# for i,color in enumerate(colors):
#     print i,'------>',color

#遍历两个表
# n = min (len(colors),len(names))
# for i in range(n):
#     print names[i],'----------->',colors[i]
# for name,color in zip(names,colors):
#     print name,'-------->',color
#高效
# for name,color in itertools.izip(names , colors):
#     print name, '---------->',color

#正序遍历
# for color in sorted(colors):
#     print color
# #倒序
# for color in sorted(colors,reverse=True):
#     print color
# #自定义
# for color in sorted(colors,key=len,reverse=True):
#     print color
# block = range(10)
# block = list(block)
# blocks = []
# while True:
#     for i in block:
#         if i == '5':
#             blocks.append(block[i])
# print blocks

#遍历字典
c = []
d = {"matthew":"blue","rachel":"green","raymond":"red"}
# for k in d :
#     print k
# for k in d.keys():
#     if k.startswith('r'):
#         c.append(k)
#         del d[k]
# print c
# print d
# #遍历字典
# for k in d :
#     print k ,'---->',d[k]

# for k , v in d.items():
#     print k,'----->',v

# for k ,v in d.iteritems():
#     print k,'---->',v

#构建字典
# d = dict (zip(names,colors))
# print d

#字典计数
D= {}
# for color in colors:
#     if color not in D:
#         D[color]=0
#     D[color]+=1
# print D

#计数并且添加到excel里边
# wb = openpyxl.Workbook()
# ws = wb.create_sheet('list')
# ws_ = wb.get_sheet_by_name('list')
# for color in colors:
#     D[color] = D.get(color,0)+1
# print D
# for i in D.keys():
#     ws.append([i,D[i]])
# wb.close()
# wb.save('1.xlsx')

#按字符串长度排序
names_ = ['raymond', 'rachel', 'matthew', 'roger','betty', 'melissa', 'judith', 'charlie']
f = {}
# for name in names_:
#     key = len(name)
#     if key not in f:
#         f[key] = []
#     f[key].append(name)
# print f

# for name in names_:
#     key = len(name)
#     f.setdefault(key,[]).append(name)
# print f

#popitem 使用
# d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
# while d:
#     key,value = d.popitem()
#     print key, '------>', value

#组合字典,,,,有问题
# defaults = {'color':'red','user':'gest'}
# paser = argparse.ArgumentParser()
# paser.add_argument('-u','--user')
# paser.add_argument('-c','--color')
# namespace = paser.parse_args([])
# command_line_args ={k:v for k,v in vars(namespace).items()if v}
#
# d= defaults.copy()
# d.update(os.environ)
# d.update(command_line_args)

#优化  元祖，列表
# p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'
# p = ['Raymond', 'Hettinger', 0x30, 'python@example.com']
# fname = p[0]
# lname = p[1]
# age = p[2]
# email = p[3]
# fname, lname, age, email = p
# print  fname,lname,age,email

# def fibonacci(n):
#     x = 0
#     y = 1
#     for i in range(n):
#         print x
#         t = y
#         print t
#         y = x + y
#         print y
#         x = t
#         print x
# u=fibonacci(2)
# 更好的方法
#
# def fibonacci(n):
#     x, y = 0, 1
#     for i in range(n):
#         print x
#         x, y = y, x + y

# 结果
# 0
# 1
# 1
# 1
# 1
# 1
# 2
# 1


# 字符串合并
# names = ['raymond', 'rachel', 'matthew', 'roger',
#          'betty', 'melissa', 'judith', 'charlie']
#
# s = names[0]
# for name in names[1:]:
#     s += ','+name
# print s
#更好方法
# print ','.join(names)


#更新序列 列表，，，，
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']
#
# # del names[0]
# # print names
# print names.pop(0)
# print names
# names.insert(0,'mar')
# print names

# 简单爬虫。。。。。
# def web_lookup(url, saved={}):
#     if url in saved:
#         return saved[url]
#     page = urllib.urlopen(url).read()
#     saved[url] = page
#     return page
# a = web_lookup('http://www.baidu.com')
#
# a = BeautifulSoup.BeautifulSoup(a)
# # print a.title
# # print a.a
# # print a.p
# print a.a.attrs


# 数据备份
# def getcontext():
#
# old_context = getcontext().copy()
# getcontext().prec = 50
# print decimal(355) / decimal(113)
# setcontext(old_context)

# 列表操作
# lis= ['0', '1', '2', '3333']
# path = u'E:/workspace/python2.7/test1/123.txt'
# f = open(path).readlines()
# for i in lis:
#     if i not in f:
#         print i, 'is not in lis'
#         continue
#     print i, 'is in lis'


# 加锁。。。。。。。。。
# lock = threading.Lock
# lock.acquire()
# try:
#     print 'Critical section 1'
#     print 'Critical section 2'
# finally:
#     lock.release()

data = np.random.randn(6,4)
print data

