#-*- coding: utf-8 -*-
import socket
import threading
from threading import *
screenLock = Semaphore(value=1)
import Queue
port = Queue.Queue()

def list_():
    lis=[]
    for i in range(70,81):
        lis.append(i)
    return lis

def _TCP_connect(ip,port_numbers,delay,output):
    for port_number in port_numbers:
        Tcp_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        Tcp_sock.settimeout(delay)
        try:
            result = Tcp_sock.connect_ex((ip, int(port_number)))
            screenLock.acquire()
            if result == 0:
                output[port_number] = 'open'
                print "%s is open from %s" % (port_number, ip)
                screenLock.release()
            else:
                output[port_number] = 'close'
                print "%s is close from %s" % (port_number, ip)
                screenLock.release()
            Tcp_sock.close()
        except socket.errno as e:
            screenLock.acquire()
            output[port_number] = 'close'
            print "%s is close from %s" % (port_number, ip)
            screenLock.release()
    return output
def _scan_ports_helper(ip,delay,output):
    port_index = 0
    _thread_limit=2500
    while port_index <len(lis):
        while threading.activeCount()< _thread_limit and port_index < len(lis):
            thread = threading.Thread(target=_TCP_connect, args = (ip,lis,delay,output))
            thread.start()
            port_index = port_index+1
        thread.join()

lis = list_()
result = {}
ips = ['220.181.112.244','220.181.112.245']
for ip in ips:
    # result[ip] = _TCP_connect(ip,lis,0.5,{})
    result_ = _scan_ports_helper(ip,1,{})
    # print ip,result
