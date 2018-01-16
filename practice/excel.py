#-*- coding: utf-8 -*-
import openpyxl
import re
import csv
import time
import datetime
name="数据筛选.xlsx"

wb = openpyxl.Workbook()
ws = wb.active
ws1 = wb.create_sheet()
ws.title = "new title"
ws.sheet_properties.tabColor = "1072BA"
ws3 = wb["new title"]
ws4 = wb.get_sheet_by_name("new title")
print ws is ws3 is ws4
print wb.get_sheet_names()

time_ = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y%m%d')
print time_



