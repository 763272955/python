# -*- coding:utf-8 -*-

import re

dict1 = {'AAAAA':'A','AAAAB':'B','AAABA':'C','AAABB':'D','AABAA':'E','AABAB':'F','AABBA':'G',
         'AABBB':'H','ABAAA':'I','ABAAB':'J','ABABA':'K','ABABB':'L','ABBAA':'M','ABBAB':'N',
         'ABBBA':'O','ABBBB':'P','BAAAA':'Q','BAAAB':'R','BAABA':'S','BAABB':'T',
         'BABAA':'U','BABAB':'V','BABBA':'W','BABBB':'X','BBAAA':'Y','BBAAB':'Z'}
dict2 = {'AAAAA':'a','AAAAB':'b','AAABA':'c','AAABB':'d','AABAA':'e,','AABAB':'f','AABBA':'g',
         'AABBB':'h','ABAAA':'i','ABAAB':'k','ABABA':'l','ABABB':'m','ABBAA':'n',
         'ABBAB':'o','ABBBA':'p','ABBBB':'q','BAAAA':'r','BAAAB':'s','BAABA':'t',
         'BAABB':'u','BABAA':'w','BABAB':'x','BABBA':'y','BABBB':'z'}
def aA(str):
    str_pg = ''
    for x in str:
        if 64 < ord(x) < 90:
            str_pg += 'B'
        if 96 < ord(x) < 122:
            str_pg += 'A'
    return str_pg
def aB(str):
    str_pg = ''
    for x in str:
        if 64 < ord(x) < 90:
            str_pg += 'A'
        if 96 < ord(x) < 122:
            str_pg += 'B'
    return str_pg
def ABC_CBA(str_pg):
    str_pg_ = ''
    for x in str_pg:
        str_pg_ = x + str_pg_
    return str_pg_
def decode(str_pg, dict):
    cout =''
    split_ = re.compile(r'.{5}')
    list = split_.findall(str_pg)
    for x in list:
        if x not in dict.keys():
            cout += '_'
        else:
            cout += dict[x]
    return cout
if __name__ == "__main__":
    str = "rEmEMbER Me,Be ToGetHer."
    str_pg = aA(str)
    str_pg_ = ABC_CBA(str_pg)
    print decode(str_pg, dict1)
    print decode(str_pg, dict2)
    print decode(str_pg_, dict1)
    print decode(str_pg_, dict2)
    str_pg = aB(str)
    str_pg_ = ABC_CBA(str_pg)
    print decode(str_pg, dict1)
    print decode(str_pg, dict2)
    print decode(str_pg_, dict1)
    print decode(str_pg_, dict2)