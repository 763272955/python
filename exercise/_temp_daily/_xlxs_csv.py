# -*- coding:utf-8 -*-

import csv
import openpyxl

def Csv2Xlxs(filename):
    wb = openpyxl.Workbook()
    ws = wb.active
    f = open(filename + ".csv")
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        row_container = []
        count = 1
        for cell in row:
            try:
                cell = int(float(cell))
                row_container.append(cell)
                continue
            except:
                pass
            row_container.append(cell.decode('gbk').encode('utf-8'))
        ws.append(row_container)
    f.close()
    wb.save(filename + ".xlsx")