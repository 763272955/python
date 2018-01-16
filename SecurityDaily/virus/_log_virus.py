# -*- coding:utf-8 -*-

from _data_operat import Data_Operat as DO
import openpyxl
import re
import os

class Log_Virus(object):
    def __init__(self, time_, asset_virus, asset_branch, log):
        self.time = time_
        self.asset_virus = asset_virus
        self.asset_branch = asset_branch
        self.log = log

    def excel_Open(self):
        if not os.path.exists("logFile/" + self.time + ".xlsx"):
            self.wb_virus_log = DO().create_Newsheet(excel_name="logFile/" + self.time+ ".xlsx", sheet_name=[u"日志"])
        else:
            self.wb_virus_log = openpyxl.load_workbook("logFile/" + self.time + ".xlsx")

    def log_Operat(self):
        if not os.path.exists("logFile/" + self.time + ".xlsx"):
            ws_virus_log = DO().get_Sheet(wb=self.wb_virus_log, sheet_name=u"日志", title=[u"结构", u"IP地址", u"主机类型", u"MAC地址",
                                                                                   u"计算机名",	u"病毒名称", u"病毒类型", u"受感染文件",
                                                                                   u"感染路径", u"攻击类型", u"处理措施", u"感染类型",
                                                                                   u"时间", u"扫描类型",u"组件版本", u"操作系统"])
        else:
            ws_virus_log = self.wb_virus_log.get_sheet_by_name(u"日志")
        for log in self.log:
            log_end = list(log)
            if log_end[7] == "21":
                log_end[7] = u"已清除"
            if log_end[7] == "121":
                log_end[7] = u"已删除"
            if log_end[7] == "25":
                log_end[7] = u"已忽略"
            if log_end[7] == "22":
                log_end[7] = u"无法清除文件"
            if log_end[7] == "122":
                log_end[7] = u"无法删除文件"
            if log_end[7] == "81":
                log_end[7] = u"已加密"
            host = DO().system_Belong(ip=log[1], asset=self.asset_branch, defaulthost=u"未知设备")
            log_end.insert(2, host)
            virus = DO().virus_Belong(virus=log[4], asset=self.asset_virus, defaultvirus=u"未知病毒")
            log_end.insert(6, virus)
            U = DO().U_Belong(U=log[6])
            log_end.insert(9, U)
            operat = DO().operat_Belong(operat=log[7])
            log_end.insert(11, operat)
            ws_virus_log.append(log_end)

    def run(self):
        self.excel_Open()
        self.log_Operat()
        self.wb_virus_log.save("logFile/" + self.time + ".xlsx")
        self.wb_virus_log.close()