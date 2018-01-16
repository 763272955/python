# -*- coding:utf-8 -*-
import json

List = []
path = u'E:/工作目录/pydata-book-2nd-edition/datasets/usda_food/database.json'
file_object = open(path,'r')
set = json.load(file_object)
for i in set.keys():
    key = i
    print set[key]
