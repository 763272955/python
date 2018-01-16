# -*- coding:utf-8 -*-

import nmap
import time

nm = nmap.PortScanner()

#ret = nm.scan(hosts='219.143.234.0/24', arguments='-sP')

#for key in ret['scan'].keys():
#    print key
start = time.time()

ip = ''
file = open('1.txt')
for line in file.readlines():
    line = line.replace('\r', '')
    line = line.replace('\n', '')
    
    ip += str(line) +' '
ret = nm.scan(hosts='219.143.234.234', arguments='-sS -p 1-65535')
print ret
end = time.time()
print end-start

