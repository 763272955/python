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


loans = pd.read_csv('end_LoanStats3a.csv',encoding='gb2312')
# print loans.shape
# # print loans.head()
# print loans.dtypes
# print loans.describe() #Pandas的describe()不能统计数据类型为object的属性，部分数据int_rate和emp_length数据类型都是object，稍后分析数据时需将它们转化为类型为floate的数字类型。
used_col = ['loan_amnt','int_rate','grade','issue_d','addr_state','loan_status','purpose','annual_inc','emp_length']
used_data = loans[used_col]
# print used_data.head(5)
def not_null_count(column):  #判断某列属性是否存在缺失值
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)
column_null_count = used_data.apply(not_null_count)
# print column_null_count
used_data[used_data['loan_status'] == 'n']
used_data = used_data.dropna([6873,21814,51957])

def coding(col, codeDict):
    colCoded = pd.Series(col,copy=True)
    for key, value in codeDict.items():
        colCoded.replace(key,value,inplace=True)
    return colCoded
pd.value_counts(used_data['loan_status'])
used_data['Loan_Status_Coded'] = coding(used_data['loan_status'],{'Current':0,'Fully Paid':0,'In Grace Period':1,'Late (31-120 days)':1,
                                                                  'Charged Off' : 1})
print '\n After Coding : '
pd.value_counts(used_data['Loan_Status_Coded'])
[i for i in pd.value_counts(used_data['Loan_Status_Coded'])]
attr = ['正常','违约']
pie = Pie('贷款状态占比')
pie.add('',attr,[int(i) for i in pd.value_counts(used_data['Loan_Status_Coded'])],is_label_show=True)
pie