#-*- coding: utf-8 -*-
import time
import datetime

start_time  = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d") + " 00:00:00"
print start_time


data1 = time.localtime()
# time.sleep(3)
data2 =time.time()
print data1
print data2
print time.strftime('%Y-%m-%d %H:%M:%S',data1)
# data = int('data2') -int('data1')

# print data
# print time.strftime('%y-%m-%d %H:%M:%S',data)
