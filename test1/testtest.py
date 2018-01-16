# -*- coding:utf-8 -*-


# from  selenium  import webdriver
# import  time
# import current
#
#
# web = webdriver.Firefox()
# web.get('http://developer.baidu.com/map/jsdemo.htm#c1_15')
import urllib2

IP = ["北京","上海"]
for i in IP:
    i= urllib2.quote(i)
    flag = 0
    file= open('1.txt','w')
        # for IP in list_num:
        #     number = dic_IP[IP]
        #     number=str(number)
    res ="http://api.map.baidu.com/location/ip?ip=i&ak=ASTbOTHARb9rCpTfAVxUt19lWnCGoNu2&coor=bd09ll"
    res = res.decode()
    res = urllib2.urlopen(res)
    a= res.read()
    zidian = eval(a)
    flag = flag +1
    if (zidian['status'] == 0):
                lng =zidian['content']['point']['x']
                lat = zidian['content']['point']['y']
                print lng,lat
                str_temp = '{"lat":'+lat+',"lng":'+lng+'}, \n'
                file.write(str_temp)
    file.close()