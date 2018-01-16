# -*- coding:utf-8 -*-

from web_.spider_web_allLink import html_download
from web_.spider_web_allLink import html_parse
from web_.spider_web_allLink import link_manage
from web_.spider_web_allLink import results_print

class Spider_Main(object):
    def __init__(self):
        self.links = link_manage.LinkManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parse.HtmlPaser()
        self.r_printer = results_print.R_printer()
    def craw(self, url):
        count = 1
        self.links.link_add_new(url)
        while self.links.link_has_new():
            link_new = self.links.link_get_new()
            try:
                html_content = self.downloader.downloader(link_new)
                links_new = self.parser.parser(link_new, html_content)
                self.links.links_add_new(links_new)
                self.r_printer.data_print_one(link_new)
                print "%d, %s" % (count, link_new)
                count += 1
            except :
                print "Craw failed : %s" % link_new
        # self.r_printer.data_print()
if __name__ == "__main__":
    url = 'http://192.168.130.130:81/'
    obj_craw = Spider_Main()
    obj_craw.craw(url)