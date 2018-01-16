# -*- coding:utf-8 -*-


import numpy as np
import pandas as pd
import openpyxl


k=[]
l={}
wb = openpyxl.load_workbook(u'E:/工作目录/123.xlsx')
ws = wb.get_sheet_by_name('LoanStats3a')
for row in ws.rows:
    print row[2].value