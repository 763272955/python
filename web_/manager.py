# -*- coding:utf-8 -*-

import threading
import Queue

threadLock = threading.Lock()
links = Queue.Queue()
exitFlag = 0
count =1

class Spider_SQL(threading.Thread):
    def __init__(self, server, link):
        threading.Thread.__init__(self)
        self.server = server
        self.link = link
        self.port = 0
        self.ports = ports

def scan(link_, server, thread_num):
    global exitFlag
    threads = []
    for x in link_:
        links.put(x)
    for x in range(int(thread_num)):
        thread = Spider_SQL(links)
        thread.setDaemon(True)
        threads.append(thread)
    for x in threads:
        x.start()
    while not links.empty():
        pass
    exitFlag = 1
    for x in threads:
        x.join()
    exitFlag = 0