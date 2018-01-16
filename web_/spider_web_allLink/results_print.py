# -*- coding:utf-8 -*-
class R_printer(object):
    def __init__(self):
        self.datas = []
    def data_collection(self, data):
        if data is None:
            return
        else:
            self.datas.append(data)
            print data
    def data_print_all(self):
        with open('all_links.txt', 'a')  as file:
            for data in self.datas:
                file.write(data + '\n')
    def data_print_one(self, link):
        with open('all_links.txt', 'a')  as file:
            file.write(link + '\n')