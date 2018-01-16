#-*- coding: utf-8 -*-

for i in range(1,10):
    for j in range(1,10):
        k=i*j
        print '%d * %d = %d ' %(j,i,k),
        if i == j:
            print
            break