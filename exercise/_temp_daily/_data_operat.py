# -*- coding:utf-8 -*-

import openpyxl

class Data_Operat(object):
    def __init__(self):
        pass

    def get_Data(self, rows):
        data = []
        for row in rows:
            data.append(row.value)
        return data

    def create_Newsheet(self, excel_name=None, sheet_name=None):
        wb = openpyxl.load_workbook(excel_name)
        for name in sheet_name:
            try:
                wb.remove_sheet(wb.get_sheet_by_name(name))
            except:
                pass
            wb.create_sheet(name)
        try:
            wb.remove_sheet(wb.get_sheet_by_name("Sheet"))
        except:
            pass
        return wb

    def get_Sheet(self, wb=None, sheet_name=None, title=None):
        ws = wb.get_sheet_by_name(sheet_name)
        ws.append(title)
        return ws

    def system_Belong(self, ip=None, asset=None, defaulthost=None):
        ip_split = ip.split('.')
        equipment = defaulthost
        for data in asset:
            data_S_split = data[-2].split('.')
            data_O_split = data[-1].split('.')
            if ip_split[0:3] == data_S_split[0:3]:
                if int(ip_split[-1]) >= int(data_S_split[-1]) and int(ip_split[-1]) <= int(data_O_split[-1]):
                    equipment = data[1]
        return equipment

    def virus_Belong(self, virus=None, asset=None, defaultvirus=None):
        virus = virus.split("_")
        virus_type = defaultvirus
        virus_ = ''
        if len(virus) > 1:
            for x in range(len(virus)-1):
                virus_ += '_' + virus[x]
            virus_ = virus_[1:]
        else:
            virus_ = virus[0]
        for asset_ in asset:
            if virus_ == asset_[0]:
                virus_type = asset_[1]
        return virus_type

    def U_Belong(self, U=None):
        if U == None:
            return u"未知类型"
        U = U.split(':')
        if len(U) == 1:
            return u"U盘"
        if U[0] != "C" and (U[1] == "\\" or U[1] =="/"):
            return u"U盘"
        return u"非U盘"

    def operat_Belong(self, operat=None):
        if operat == u"已删除" or operat == u"已清除":
            return u"接触"
        return u"感染"

    def dict_Count(self, dict=None, key=None, ):
        if key not in dict.keys():
            dict[key] = 1
        else:
            dict[key] += 1
        return dict

    def dict_Getdata(self, ws=None, dict=None):
        count = 0
        for key in dict.keys():
            count += dict[key]
        for key in dict.keys():
            percent = float(dict[key])/float(count)
            ws.append([key, dict[key], percent])
        return ws