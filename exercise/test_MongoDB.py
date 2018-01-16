# -*- coding:utf-8 -*-

import socket
import pymongo

def host2ip(url):
    url_ip = socket.gethostbyname(url)
    return url_ip
def poc(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        result = s.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
    except:
        print "conn failed"
def testConn(ip, port):
    try:
        conn = pymongo.MongoClient(ip, port, socketTimeoutMS = 3000)
        dbname = conn.database_names()
        print "dbname:"
        print dbname
        db = conn['topsites_sx']
        tables = db.collection_names()
        print "topsites_sx 's tables:"
        print tables
        if dbname:
            return True
    except:
        print "DBconn failed"
        return False
# def testCreate(ip, port):
#     try:
#         conn = pymongo.MongoClient(ip, port, socketTimeoutMS = 3000)
#         admin = conn.admin
#         if admin:
#     except:
#         print "create failed"
#         return False
if __name__ == "__main__":
    url = 'www.baidu.com'
    port = 27017
    url_ip = '192.168.130.139'
    if poc(url_ip, port):
        if testConn(url_ip, port):
            print '%s Succeed!' % url_ip
        else:
            print '%d port is open but can\'t connect ' % port
    else:
        print '%d port is not open ,You can try other port' % port
