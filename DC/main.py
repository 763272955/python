# -*- coding:utf-8 -*-

import os
import urlparse
from methods import google_
from methods import see_page
import sys
reload(sys)
sys.setdefaultencoding("utf-8" )

class DC_Main(object):
    def __init__(self, url):
        self.url = url
        self.keyword = []
        self.google = ['inurl:', 'site:']

    def get_Keyword(self):
        file = open('keyword.txt', 'r')
        key = file.readlines()
        for k in key:
            k = k.replace('\n', '')
            if k == '':
                continue
            self.keyword.append(k)

    def run(self):
        self.get_Keyword()
        e_main = ''
        print u'====== 检测网站 ======'
        print 'url: %s' % self.url
        try:
            obj = see_page.See_MainPage(self.url, self.keyword)
            reason = obj.run()
        except IOError, e:
             e_main = e.message
        print '_______________________'
        try:
            obj = google_.Google(self.url, self.google, self.keyword)
            print u'== google搜索暗链地址 =='
            dc = obj.run()
            if e_main == '':
                if len(dc) == 0 and reason == False:
                    file = open('output/no.txt', 'a+')
                    file.write(self.url + '\n')
                    file.close()
                elif len(dc) !=0 and reason == False:
                    file = open('output/' + urlparse.urlparse(self.url).netloc + '.txt', 'a+')
                    file.write(u"主页未发现暗链" + '\n')
                    file.write("________________________________" + '\n')
                    for x in dc:
                        file.write(x + '\n')
                    file.close()
                else:
                    file = open('output/' + urlparse.urlparse(self.url).netloc + '.txt', 'a+')
                    file.write("________________________________" + '\n')
                    for x in dc:
                        file.write(x + '\n')
                    file.close()
            else:
                if len(dc) != 0:
                    file = open('output/' + urlparse.urlparse(self.url).netloc + '.txt', 'a+')
                    file.write(u"主页连接失败, 原因: %s" % e_main + '\n')
                    file.write("________________________________" + '\n')
                    for x in dc:
                        file.write(x + '\n')
                    file.close()
                else:
                    file = open('output/no.txt', 'a+')
                    file.write(self.url + '\n')
                    file.close()
            print '_______________________'
        except IOError, e:
            e_google = e.message
            print e_google

if __name__ == "__main__":
    file = open('url.txt', 'r')
    for url in file.readlines():
        url = url.replace('\n', '')
        if url == '':
            continue
        url_parser = urlparse.urlparse(url)
        if url_parser.scheme != '':
            url = url_parser.netloc
        if os.path.exists('output/' + url + '.txt'):
            file = open('output/' + url + '.txt', 'w')
            file.write('')
            file.close()
        url_parser = urlparse.urlparse(url)
        if url_parser.scheme == '':
            url = 'http://' + url
        DC_Main(url).run()
    file.close()