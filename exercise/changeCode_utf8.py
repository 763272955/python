# -*- coding:utf-8 -*-

import base64
import binascii

def b64encode(str):
    return base64.b64encode(str)
def b32encode(str):
    return base64.b32encode(str)
def b16encode(str):
    return base64.b16encode(str)
def b64decode(str):
    return base64.b64decode(str)
def b32decode(str):
    return base64.b32decode(str)
def b16decode(str):
    return base64.b16decode(str)
def u2g(str):
    return str.decode('utf-8').encode('gbk')
def g2u(str):
    return str.decode('gbk').encode('utf8')
def s2hex(str):
    return str.encode('hex')
def hex2s(str):
    return str.decode('hex')
if __name__ == "__main__":
    str = 'ORLL/XHG8v2PjEwiTnYZz6xNT9BcmHNqhLUSh7H1trhZX7XvnxIZj1spuDPtUtnwYZpRPpZL2aVJ'
    str = str[::-1]
        # file = open('my.txt','r')
    # str = file.readline()
    # print str
    print s2hex(b64decode(str))
    print b64decode(str).decode('unicode_escape')
    print b64decode(str)
    print b32decode(str)
    # print b16decode(str)
    # print s2hex(b64decode(str))
    # print s2hex(u2g(b64decode(str)))
    # print s2hex(b32decode(str))
    # print s2hex(u2g(b32decode(str)))
    # print s2hex(b16decode(str))
    # print s2hex(u2g(b16decode(str)))
    # print b64encode(str)
    # print b32encode(str)
    # print b16encode(str)
