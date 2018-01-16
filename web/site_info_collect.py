__author__ = 'AZONE'
import urllib2
import re
import sys
from bs4 import BeautifulSoup
from save_to_mysql import addurls
from dirfuzz import fuzz_start
from site_port_check import portScan
import time
import os
urllist =[]
iplist =[]
reload(sys)
sys.setdefaultencoding('utf-8')
def get_url(body_text):

        soup=BeautifulSoup(body_text)
        links=soup.findAll('a')
        for link in links:
            url =link.get('href')
            try:
                if '?' in str(url):
                    urllist.append(url)
            except:
                pass


def get_ip(body_text):
    body_text=body_text.replace(" ","")
    ips=re.findall(r"\d+\.\d+\.\d+\.\d+",body_text,re.I)
    for i in ips:
        iplist.append(i)
def get_post(body_text):
    pass
def get(target_url):
    try:
        i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48','Upgrade-Insecure-Requests':'1','Referer':'http://toutiao.com/m5573658957/'}
        req = urllib2.Request(target_url,headers=i_headers)
        body_text=urllib2.urlopen(req).read()
    except:
        pass
    return body_text
def subdomainapi(target_url):
    if 'www' in target_url:
        try:
            subdomain = []
            target_url = target_url.strip('http:').strip('/').strip('www.')
            api = 'http://i.links.cn/subdomain/'+target_url+'.html'
            i_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.48'}
            req = urllib2.Request(api,headers=i_headers)
            body_text=urllib2.urlopen(req).read()
            soup=BeautifulSoup(body_text)
            links=soup.findAll('a')
            for link in links:
                url =link.get('href')
                if target_url in url:
                    subdomain.append(url)
            return subdomain
        except:
            pass
    else:
        return None

def runscan(target_url):
    global urllist
    global iplist
    urllist = []
    turllist = []
    iplist =[]
    list1 = []
    list2 = []

    body_text = get(target_url)
    get_ip(body_text)
    get_url(body_text)
    iplist = list(set(iplist))
    for i in urllist:
        if 'http://' not in i:
            i = target_url + i
            list1.append(i)
        else:
            list2.append(i)
    target_urllist = list(set(list1).union(set(list2)))
    collect_dirs = fuzz_start(target_url)
    collect_dirs= list(set(collect_dirs))
    collect_ports = portScan(target_url)
    subdomain = subdomainapi(target_url)

    addurls(str(target_url),str(target_urllist),str(iplist),str(collect_dirs),str(collect_ports),str(subdomain))
    return target_urllist,iplist,collect_dirs,collect_ports,subdomain
#runscan('http://mooc.hlju.edu.cn/')