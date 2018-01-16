# -*- coding:utf-8 -*-

import requests
import os
import urlparse
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class See_MainPage(object):
    def __init__(self, url, PROBES):
        self.url = url
        self.PROBES = PROBES
        self.dc = set()

    def content_Get(self):
        with requests.session() as s:
            response = s.get(self.url, timeout=10)
            encodings = requests.utils.get_encodings_from_content(response.content)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = response.apparent_encoding
            html_content = response.content.decode(encoding, 'replace')
        return html_content

    def content_Parse(self):
        html_content = self.content_Get()
        if html_content is not None:
            soup = BeautifulSoup(html_content, 'html.parser')
            a = soup.find_all('a')
            return a

    def run(self):
        a = self.content_Parse()
        for a_ in a:
            text = a_.get_text()
            for probe in self.PROBES:
                if probe in text:
                    if urlparse.urlparse(a_['href']).netloc != urlparse.urlparse(self.url).netloc \
                            and len(urlparse.urlparse(a_['href']).netloc) != 0:
                        print u"关键字: %s , 页面: %s"  % (probe, self.url)
                        file = open('output/' + urlparse.urlparse(self.url).netloc + '.txt', 'a')
                        file.write(u"关键字: %s , 页面: %s"  % (probe, self.url) + '\n')
                        file.close()
                        return True
        return False