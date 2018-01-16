# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import  seaborn as sns
sns.set_style('whitegrid')
# %matplotlib inline
from  pyecharts import  Pie
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_csv('LoanStats3a.csv',encoding = 'latin-1', skiprows = 1)   #把csv变成矩阵
# print data.shape  #统计行数列数
# print data.head  #默认统计前5行
# print data.iloc[0] #取矩阵中第一行样本

def not_null_count(column):  #判断某列属性是否存在缺失值
    column_null = pd.isnull(column)
    null = column_null[column_null]
    return len(null)
column_null_count = data.apply(not_null_count)
# print (column_null_count)
half_count = len(data)/2 #设定阈值
data = data.dropna(thresh= half_count,axis = 1) #若某一列数据缺失的数量超过阈值就会被删除
#data = data.dropna(['desc','url'],axis = 1) #删除某些加载了网址的url和描述的列
data.to_csv('end_LoanStats3a.csv',index = False) # 将预处理后的数据转化为csv
