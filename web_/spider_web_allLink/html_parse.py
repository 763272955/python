# -*- coding:utf-8 -*-

import re
import urlparse
from bs4 import BeautifulSoup

class HtmlPaser(object):
    def _get_links(self, link_s, soup):
        links_new = set()
        links = soup.find_all('a')
        for link_d in links:
            try:
                if link_d['href'] is None:
                    print 'Craw failed , this is href is none'
                    continue
            except:
                print 'Craw failed , there is no href'
                continue
            link_s_netloc = urlparse.urlparse(link_s).netloc
            link_d_netloc = urlparse.urlparse(link_d['href']).netloc
            if link_s_netloc == link_d_netloc or len(link_d_netloc) == 0:
                if link_d['href'] == 'index.asp':
                    continue
                else:
                    link = urlparse.urljoin(link_s, link_d['href'])
                    links_new.add(link)
        return links_new

    def parser(self, link, html_content):
        if html_content is None or link is None:
            return
        else:
            soup = BeautifulSoup(html_content, 'html.parser')
            links_new = self._get_links(link, soup)
            return links_new