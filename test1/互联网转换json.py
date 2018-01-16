# -*- coding:utf-8 -*-

import openpyxl
import json
import codecs
import collections
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')




filename = datetime.datetime.now().strftime('%Y%m%d')
def network_(filename):
    f = codecs.open(filename,'w', 'utf-16')
    title = [u"告警时间", u"规则名称", u"源IP",u"源端口",u"目的IP",u"目的端口",u"上报引擎",u"返回消息",u"网口编号",u"别名"]
    # time_index = title.index(u"告警时间")
    # rule_index = title.index(u"规则名称")
    YIP_index = title.index(u"源IP")
    # MIP_index = title.index(u"目的IP")
    # Yport_index = title.index(u"源端口")
    # Mport_index = title.index(u"目的端口")
    # report_index = title.index(u"上报引擎")
    # response_index = title.index(u"返回消息")
    # number_index = title.index(u"网口编号")
    # alias_index = title.index(u"别名")

    wb = openpyxl.load_workbook(u"E:/工作目录/互联网.xlsx")
    ws = wb.get_sheet_by_name("Sheet1")
    # ws.append(title)
    # ws.append(["1", "2", "3"])
    # ws.append([4, 5, 6])
    # ws.append([7, 8, 9])

    json_dict = collections.OrderedDict()

    for row in list(ws.rows)[1:]:
        # json_dict[title[time_index]] = str(row[time_index].value)
        # json_dict[title[rule_index]] = str(row[rule_index].value)
        json_dict[title[YIP_index]] = str(row[YIP_index].value)
        # json_dict[title[Yport_index]] = str(row[Yport_index].value)
        # json_dict[title[MIP_index]] = str(row[MIP_index].value)
        # json_dict[title[Mport_index]] = str(row[Mport_index].value)
        # json_dict[title[report_index]] = str(row[report_index].value)
        # json_dict[title[response_index]] = str(row[response_index].value)
        # json_dict[title[number_index]] = str(row[number_index].value)
        # json_dict[title[alias_index]] = str(row[alias_index].value)

        # print >>f,"%s" % (json_dict)
        write = json.dumps(json_dict, ensure_ascii=False)
        # write = title[time_index]
        code_='{"index":{"_index":"logstash_test4","_type":"logstash_test4"}}'
        print write
        # print >>f ,"%s" % (code_)
        print >>f,"%s" % (write)
        # f.write(write)
        # f.write('\n')
    f.close()
network_(filename)