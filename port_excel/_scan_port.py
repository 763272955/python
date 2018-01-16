# -*- coding:utf-8 -*-

import socket
import threading
screenLock = threading.Semaphore(value=1)

class Scan_Main():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
    def scan_port(self):
        socket.setdefaulttimeout(0.5)
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            response = conn.connect_ex((self.ip, self.port))
            if response == 0:
                screenLock.acquire()
                print "%s is open from %s" % (self.port, self.ip)
                screenLock.release()
                return True
            conn.close()
            return False
        except:
            conn.close()
            return False


    def run(self):
        if self.scan_port():
            return True
        return False
