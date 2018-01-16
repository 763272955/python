# -*- coding:utf-8 -*-

import openpyxl

class Excel_Creat(object):
    def __init__(self):
        pass

    def excel_Virus(self):
        wb = openpyxl.Workbook()
        wb.save(u"out.xlsx")
        wb.close()

    # def excel_Log(self):
    #     wb = openpyxl.Workbook()
    #     wb.save(u"logFile/" + self.time + u".xlsx")
    #     wb.close()

    def run(self):
        self.excel_Virus()