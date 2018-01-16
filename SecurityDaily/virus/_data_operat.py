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

    def system_Belong(self, ip=None, asset=None):
        ip_split = ip.split('.')
        branch = u"未知分行"
        qu = u"未知区域"
        equipment = u"未知设备"
        class_ = u"未知类型"
        for data in asset:
            data_S_split = data[3].split('.')
            data_O_split = data[4].split('.')
            if ip_split[0:3] == data_S_split[0:3]:
                if int(ip_split[-1]) >= int(data_S_split[-1]) and int(ip_split[-1]) <= int(data_O_split[-1]):
                    class_ = data[5]
                    equipment = data[2]
                    branch = data[0]
                    qu = data[1]
        return equipment, branch, qu, class_

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
            if virus == asset_[0]:
                virus_type = asset_[1]
        return virus_type

    def handle_result(self, code=None):
        code = str(code)
        if code == "21":
            return u"已清除"
        if code == "121":
            return u"已删除"
        if code == "25":
            return u"已忽略"
        if code == "22":
            return u"无法清除文件"
        if code == "122":
            return u"无法删除文件"
        if code == "81":
            return u"已加密"

    def detect_result(self, code=None):
        code = str(code)
        if code == "11":
            return u"实时扫描"
        if code == "13":
            return u"预设扫描"
        if code == "12":
            return u"手动扫描"
        if code == "1":
            return u"DCS"

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