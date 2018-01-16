# -*- coding:utf-8 -*-

import socket
import argparse
import sys
from threading import *
screenLock = Semaphore(value=1)
import Queue
port = Queue.Queue()

ports_descript = 'Ports scan \
                Example 1: -P 80,81,82,83,84,85,86,87,88 \
                Example 2: -P 80-88 \
                Example 3: -P 80-84,85-88'
Default_Ports = '21,22,23,25,80,81,110,135,139,443,445,1433,1434,1521,'\
                '2433,3306,3307,3389,5800,5900,8080,25666,27017,28017'

class Scan_Main(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip
        self.ports = set()
        self.t_number = ''
    def scan_port(self):
        while not port.empty():
            port__ = port.get()
            socket.setdefaulttimeout(1)
            conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            response = conn.connect_ex((self.ip, port__))
            if response == 0:
                try:
                    results_ = conn.recv(1024)
                    results = results_.replace("\n", "")
                    file = open('log/' + self.ip + '_log.txt', 'a+')
                    file.write('[+] %d /tcp open  ' % port__ + '[+] ' + str(results) + '\n')
                    file.close()
                    screenLock.acquire()
                    print '[+] %d /tcp open  ' % port__ + '[+] ' + str(results)
                except:
                    file = open('log/' + self.ip + '_log.txt', 'a+')
                    file.write('[+] %d /tcp open  [-] Unknown' % port__ + '\n')
                    file.close()
                    screenLock.acquire()
                    print '[+] %d /tcp open  [-] Unknown' % port__
                finally:
                    screenLock.release()
                    conn.close()
            else:
                file = open('log/' + self.ip + '_log.txt', 'a+')
                file.write('[-] %d /tcp close' % port__ + '\n')
                file.close()
                screenLock.acquire()
                print '[-] %d /tcp close' % port__
                screenLock.release()
    def run(self):
        self.scan_port()

class Divide_Ports(object):
    def __init__(self):
        self.ports = ''
    def divide_port(self):
        port_ = set()
        ports = self.ports.split(',')
        for x in ports:
            ports_ = x.split('-')
            if len(ports_) == 1:
                if ports_[0].isdigit():
                    port_.add(int(ports_[0]))
                    continue
            if ports_[0].isdigit() and ports_[1].isdigit():
                for x in range(int(ports_[0]), int(ports_[1])+1):
                    port_.add(x)
                continue
            print "Your Ports is illegal"
            print parser.format_usage()
            sys.exit()
        return port_
    def run(self, ports):
        self.ports = ports
        ports_ = self.divide_port()
        return ports_

if __name__ == "__main__":
    port_divide = Divide_Ports()
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', help='ip address', type=str)
    parser.add_argument('-P', '--port', help=ports_descript, type=str, default=Default_Ports)
    parser.add_argument('-T', '--thread', help='Thread number, Default number is 1', type=str, default='1')
    args = parser.parse_args()
    if args.host == None:
        print parser.format_usage()
        sys.exit()
    ip = args.host
    thread_num = args.thread
    ports = port_divide.run(args.port)
    try:
        threads = []
        for x in ports:
            port.put(x)
        for x in range(int(thread_num)):
            task = Scan_Main(ip)
            threads.append(task)
        for task in threads:
            task.setDaemon(True)
            task.start()
        for task in threads:
            task.join()
        print "Scan END!"
    except:
        print "Scan END BY SOMETHING!"