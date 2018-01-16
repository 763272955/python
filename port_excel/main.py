# -*- coding:utf-8 -*-

import _divide_IP
import time
import _scan_port
import _result_record
import threading
import Queue
PORT_ = Queue.Queue()
import nmap

print u"===================================================="
print u"Usage:"
print u"----------------------------------------------------"
print u" 1.扫描单个IP,输入单个IP地址:"
print u"   eg:10.124.5.20"
print u"----------------------------------------------------"
print u" 2.扫描多个IP,输入多个IP,以','分开:"
print u"   eg:10.124.5.20,10.124.5.21"
print u"----------------------------------------------------"
print u" 3.扫描范围IP,以'-'分开:"
print u"   eg:10.124.5.20-10.124.5.25"
print u"----------------------------------------------------"
print u" 4.批量扫描范围IP,以','分开:"
print u"   eg:10.124.5.1-10.124.5.5,10.124.5.15-10.124.5.20"
print u"----------------------------------------------------"
print u" 5.扫描IP段,将IP结尾标记为'0':"
print u"   eg:10.124.5.0"
print u"===================================================="
print u"                                                    "

result_ = {}
ports_ = []

def get_Port(ip, port):
        if _scan_port.Scan_Main(ip, port).run():
            ports_.append(port)

def task_Thread(ip, thread_num):
    while threading.activeCount() <= thread_num:
        while not PORT_.empty():
            port = PORT_.get()
            task_get = threading.Thread(target=get_Port, args=(ip, port,))
            task_get.start()
        else:
            return

if __name__ == "__main__":
    starttime = time.time()
    IP_ = raw_input(u"请输入扫描IP: ".encode('gbk'))
    IP = _divide_IP.Divide_IP().run(IP_)
    thread_num = raw_input(u"请输入线程数(默认3000): ".encode('gbk'))
    #IP = []
    #nm = nmap.PortScanner()
    #ret = nm.scan(hosts='219.143.234.0/24', arguments='-sP')
    #for key in ret['scan'].keys():
    #    IP.append(key)
    if len(thread_num) !=0 and thread_num.isdigit():
        thread_num = int(thread_num)
    else:
        thread_num = 3000

    while True:
        try:
            for ip in IP:
                ports = []
                for x in range(0, 65535):
                    ports.append(x)
                ports_ = []
                for x in ports:
                    PORT_.put(x)
                task_ = threading.Thread(target=task_Thread, args=(ip, thread_num,))
                task_.setDaemon(True)
                task_.start()
                task_.join()
                print "%s SCAN END" % ip
                if len(ports_) != 0:
                    result_[ip] = ports_
                else:
                    result_[ip] = "NULL"
            break
        except:
            pass
    print result_
    end_time = time.time()
    _result_record.result_Record(result_)
    print end_time - starttime
