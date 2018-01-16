# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urlparse
import datetime
import math
import itertools
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class Google(object):
    def __init__(self, url_test, google, PROBES):
        self.starttime = datetime.datetime(1970, 1, 1, 8, 0)
        self.url_test = url_test
        self.google = google
        self.PROBES = PROBES
        self.dc = set()

    def url_Make(self):
        url_ = []
        url_list = []
        endtime = datetime.datetime.now()
        nowtime = int(math.floor((endtime - self.starttime).total_seconds()))
        time = ['http://www.baidu.com/s?gpc=stf=' + str(nowtime - 2678400) + ',' + str(nowtime) + '|stftype=1&wd=',
                'http://www.baidu.com/s?wd=']
        url_.append(urlparse.urlparse(self.url_test).netloc)
        for item in itertools.product(time, self.google, url_):
            data = ''.join(item)
            url_list.append(data)
        return url_list

    def content_Get(self, url):
        try:
            with requests.session() as s:
                response = s.get(url)
                encodings = requests.utils.get_encodings_from_content(response.content)
                if encodings:
                    encoding = encodings[0]
                else:
                    encoding = response.apparent_encoding
                html_content = response.content.decode(encoding, 'replace')
            return html_content
        except IOError, e:
            print e.message


    def url_Judge(self, true_url):
        if urlparse.urlparse(self.url_test).netloc == urlparse.urlparse(true_url).netloc:
            return True
        if urlparse.urlparse(self.url_test).path == urlparse.urlparse(true_url).netloc:
            return True
        return False

    def dc_Judge(self, text, true_url):
        if u'百度' in text and u'知道' in text:
            if self.url_Judge(true_url):
                if true_url not in self.dc:
                    print u"暗链地址: %s" % true_url
                self.dc.add(true_url)
                return
        for probe in self.PROBES:
            if probe in text:
                if self.url_Judge(true_url):
                    if true_url not in self.dc:
                        print u"暗链地址: %s" % true_url
                    self.dc.add(true_url)
                    return

    def content_Parse(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        page = soup.find_all('h3', class_="t")
        next = soup.find_all('a', class_="n")
        for page_ in page:
            a = page_.find('a')
            text = a.get_text()
            link = a['href']
            true_url = requests.get(link, allow_redirects=False).headers.get('location')
            self.dc_Judge(text, true_url)
        for next_ in next:
            if u'下一页' in next_.get_text():
                return "http://www.baidu.com" + next_["href"]

    def dc_Parse(self, url):
        html_content = self.content_Get(url)
        url_next = self.content_Parse(html_content)
        if url_next is not None:
            self.dc_Parse(url_next)

    def run(self):
        url_list = self.url_Make()
        for url in url_list:
            self.dc_Parse(url)
        return self.dc