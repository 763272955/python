# -*- coding:utf-8 -*-

class Divide_IP(object):
    def __init__(self):
        self.ip = []

    def split_Minus(self, IP_):
        IP_ = IP_.split('-')
        try:
            start = IP_[0].split('.')[-1]
            end = IP_[1].split('.')[-1]
            for x in range(int(start), int(end)+1):
                str_ = ''
                for y in range(3):
                    str_ += IP_[0].split('.')[y] + '.'
                str_ += str(x)
                self.ip.append(str_)
        except:
            print u"错误: 请检查IP输入正确!"

    def split_Comma(self, IP_):
        IPs = []
        IP_ = IP_.split(',')
        for x in IP_:
            IPs.append(x)
        return IPs

    def run(self, IP_):
        self.__init__()
        print IP_
        if '-' in IP_ and ',' not in IP_:
            self.split_Minus(IP_)
            return self.ip
        if '-' in IP_ and ',' in IP_:
            IPs = self.split_Comma(IP_)
            for x in IPs:
                self.split_Minus(x)
            return self.ip
        if ',' in IP_ and '-' not in IP_:
            IPs = self.split_Comma(IP_)
            for x in IPs:
                self.ip.append(x)
            return self.ip
        else:
            x = IP_.split('.')
            if x[-1] == '0':
                for y in range(1, 255):
                    str_ = ''
                    for m in range(3):
                        str_ += x[m] + '.'
                    str_ += str(y)
                    self.ip.append(str_)
                return self.ip
            self.ip.append(IP_)
            return self.ip