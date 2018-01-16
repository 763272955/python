# -*- coding:utf-8 -*-

import datetime
import openpyxl

def sheet_Exist(wb, sheet_name):
    try:
        ws = wb.get_sheet_by_name(sheet_name)
        return True
    except:
        return False

def result_Record(result):
    filename = "output/Port_Excel.xlsx"
    sheet_name = datetime.datetime.now().strftime('%Y%m%d')
    wb = openpyxl.load_workbook(filename)
    if not sheet_Exist(wb, sheet_name):
        wb.create_sheet(sheet_name)
    ws = wb.get_sheet_by_name(sheet_name)
    for x in result.keys():
        test = []
        port_ = ''
        test.append(x)
        for y in result[x]:
            port_ += str(y) + ','
        test.append(port_)
        ws.append(test)
    wb.save(filename)
    wb.close()
