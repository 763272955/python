# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import itertools
import urlparse
import main
import os
import sys
import time
reload(sys)
sys.setdefaultencoding("utf8")

def collect_Url(url):
    file = open('url.txt', 'a+')
    file.write(url+'\n')
    file.close()

def content_Get(url):
    response = requests.get(url)
    response.encoding = requests.utils.get_encodings_from_content(response.content)[0]
    html_content = response.text
    return html_content

def url_Judge(true_url):
    print true_url
    collect_Url(true_url)

def content_Parse(content):
    soup = BeautifulSoup(content, 'html.parser')
    page = soup.find_all('h3', class_="t")
    next = soup.find_all('a', class_="n")
    for page_ in page:
        a = page_.find('a')
        link = a['href']
        true_url = requests.get(link, allow_redirects=False).headers.get('location')
        url_Judge(true_url)
    for next_ in next:
        if u'下一页' in next_.get_text():
            return "http://www.baidu.com" + next_["href"]

def url_Collect(url, count):
    html_content = content_Get(url)
    url_next = content_Parse(html_content)
    if count <= 30:
        count += 1
        if url_next is not None:
            url_Collect(url_next, count)

if __name__ == "__main__":
    if os.path.exists('url.txt'):
        file = open('url.txt', 'w')
        file.write('')
        file.close()
    url = set()
    baidu = ['http://www.baidu.com/s?wd=']
    search = ['inurl:.cn ']
    location = []
    file = open('location.txt', 'r')
    for x in file.readlines():
        x = x.replace('\n', '')
        if x == '':
            continue
        location.append(x)
    file.close()
    for item in itertools.product(baidu, search, location):
        data = ''.join(item)
        url.add(data)
    for url_ in url:
        url_Collect(url_, count=1)
    file = open('url.txt', 'r')
    for url in file.readlines():
        url = url.replace('\n', '')
        if url == '':
            continue
        url_parser = urlparse.urlparse(url)
        if url_parser.scheme == '':
            url = 'http://' + url
        main.DC_Main(url).run()
    file.close()
