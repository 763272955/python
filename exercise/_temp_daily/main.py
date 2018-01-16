#-*- coding:utf-8 -*-

from _data_operat import Data_Operat as DO
from _excel_create import Excel_Creat as EC
from _xlxs_csv import Csv2Xlxs
import openpyxl
import re
import sys

def data_Operat(ws_source, ws_end, index):
    ws_source = list(ws_source)[1:]
    for source in ws_source:
        source = DO().get_Data(source)
        host = None
        url = ''
        data_content = None
        data_content_code = ''
        data = []
        data.append(source[1])
        data.append(source[index-3])
        data.append(source[index-1])
        try:
            test  = source[index].split('\n')
            for x in test:
                if x == None or x == '':
                    continue
                result = re.compile(r'Host=(.*?);').findall(x)
                if len(result) != 0:
                    host = result[0]
                result = re.compile(ur'主机名称=(.*?);').findall(x)
                if len(result) != 0:
                    host = result[0]
                result = re.compile(r'URL=(.*?);').findall(x)
                if len(result) != 0:
                    url = result[0]
                result = re.compile(ur'URL名称=(.*?);').findall(x)
                if len(result) != 0:
                    url = result[0]
                result = re.compile(ur"内容=(.*?)[;?]").findall(x)
                if len(result) != 0:
                    data_content = result[0]
                    if data_content != '':
                        data_content_ = result[0].split(' ')
                        for y in data_content_:
                            if len(y) == 1:
                                y = '0' + y
                            if int(y.upper(), 16) < 32 or int(y.upper(), 16) > 126:
                                data_content_code += '\\x' + y
                                continue
                            try:
                                y.decode('hex').decode('utf-8')
                                data_content_code += y.decode('hex')
                            except:
                                data_content_code += '\\x' + y
                result = re.compile(ur"数据=(.*?)[;?]").findall(x)
                if len(result) != 0:
                    data_content = result[0]
                    if data_content != '':
                        data_content_ = result[0].split(' ')
                        for y in data_content_:
                            if len(y) == 1:
                                y = '0' + y
                            if int(y.upper(), 16) < 32 or int(y.upper(), 16) > 126:
                                data_content_code += '\\x' + y
                                continue
                            try:
                                y.decode('hex').decode('utf-8')
                                data_content_code += y.decode('hex')
                            except:
                                data_content_code += '\\x' + y
                result = re.compile(r"Body_Data=(.*?)[?;]").findall(x)
                if len(result) != 0:
                    data_content = result[0]
                    if data_content != '':
                        data_content_ = result[0].split(' ')
                        for y in data_content_:
                            if len(y) == 1:
                                y = '0' + y
                            if int(y.upper(), 16) < 32 or int(y.upper(), 16) > 126:
                                data_content_code += '\\x' + y
                                continue
                            try:
                                y.decode('hex').decode('utf-8')
                                data_content_code += y.decode('hex')
                            except:
                                data_content_code += '\\x' + y
                if '=' not in x:
                    url += ';' + x[:-1]
        except:
            pass
        data.append(host)
        data.append(url)
        data.append(data_content)
        data.append(data_content_code)
        ws_end.append(data)
    return ws_end

if __name__ == '__main__':
    jxq_filename = u'input/光大银行_酒仙桥数据中心_1012_IDS.xlsx'
    sd_filename = u'input/光大银行_上地数据中心_1012_IDS.xlsx'
    wb_jxq_source = openpyxl.load_workbook(jxq_filename)
    wb_sd_source = openpyxl.load_workbook(sd_filename)
    EC().run()
    wb_end = DO().create_Newsheet("out.xlsx", [u"上地", u"酒仙桥"])
    ws_sd = DO().get_Sheet(wb_end, u"上地", [u"事件名称", u"目IP", u"目端口", "host", "url", u"数据内容", u"数据内容解码"])
    ws_jxq = DO().get_Sheet(wb_end, u"酒仙桥", [u"事件名称", u"目IP", u"目端口", "host", "url", u"数据内容", u"数据内容解码"])
    ws_sd_souce = wb_sd_source.get_sheet_by_name(u"Sheet1")
    ws_jxq_source = wb_jxq_source.get_sheet_by_name(u"Sheet1")
    ws_jxq = data_Operat(ws_jxq_source, ws_jxq, 11)
    ws_sd = data_Operat(ws_sd_souce, ws_sd, 10)
    wb_end.save("out.xlsx")
    wb_end.close()
    wb_jxq_source.close()
    wb_sd_source.close()