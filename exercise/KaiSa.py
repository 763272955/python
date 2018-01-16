# -*- coding:utf-8 -*-

def crack_26(str):
    for x in range(1,26):
        str_ = ''
        for y in str:
            if 64 < ord(y) < 91:
                temp = (ord(y) + x) % 90
                if temp == 0:
                    temp = 90
                if temp < 26:
                    temp += 64
                str_ += chr(temp)
            elif 96 < ord(y) <123:
                temp = (ord(y) + x) % 122
                if temp == 0:
                    temp = 122
                if temp < 26:
                    temp += 96
                str_ += chr(temp)
            else:
                str_ += y
        print str_
def crack_127(str):
    for p in range(127):
        str_ = ''
        for i in str:
            temp = chr((ord(i) + p) % 127)
            if 32 < ord(temp) < 127:
                str_ = str_ + temp
                feel = 1
            else:
                feel = 0
                break
        if feel == 1:
            print str_
if __name__ == "__main__":
    str = 'jtlc{dbyn_yatji_mlelqdp3nlqg8_t7k0c}'
    crack_26(str)
    # crack_127(str)