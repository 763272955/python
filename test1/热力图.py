# -*- coding:utf-8 -*-

import urllib2
import  time
import datetime
import csv
import openpyxl
from  selenium  import webdriver



nowtime = datetime.datetime.now().strftime('%Y%m%d')
nowtimel = nowtime+".csv"
nowtime_ = nowtime+".xlsx"
nowtime = nowtime+".txt"
dic_IP={}
list_num=[]

def open_url():
    web = webdriver.Firefox()
    web.get('http://developer.baidu.com/map/jsdemo.htm#c1_15')


def Csv2Xlxs(nowtimel, nowtime_):
    wb = openpyxl.Workbook()
    ws = wb.active
    f = open(nowtimel)
    reader = csv.reader(f, delimiter='\t')
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
    wb.save(nowtime_)
def search_database():
    wb = openpyxl.load_workbook('20171221.xlsx')
    ws = wb.get_sheet_by_name('Sheet')
    for row in list(ws.rows)[1:]:
        dic_IP[row[0].value]=row[1].value
    for key in dic_IP.keys():
        list_num.append(key)
    return list_num,dic_IP

def search_IP(list_num,dic_IP):
    flag = 0
    file= open(nowtime,'w')
    for IP in list_num:
        number = dic_IP[IP]
        number=str(number)
        res =urllib2.urlopen("http://api.map.baidu.com/location/ip?ip=%s&ak=ASTbOTHARb9rCpTfAVxUt19lWnCGoNu2&coor=bd09ll" % IP)
        a= res.read()
        zidian = eval(a)
        flag = flag +1
        if (zidian['status'] == 0):
            print flag , IP
            lng =zidian['content']['point']['x']
            lat = zidian['content']['point']['y']
            print lng,lat
            str_temp = '{"lat":'+lat+',"lng":'+lng+',"count":'+number+'}, \n'
            file.write(str_temp)
    file.close()
# Csv2Xlxs(nowtimel,nowtime_)
open_url()
list_num, dic_IP = search_database()
search_IP(list_num,dic_IP)