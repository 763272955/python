# -*- coding:utf-8 -*-

datas = [[0, 0, 0, 0, 0, 'yes'],
         [0, 0, 0, 1, 0, 'no'],
         [1, 0, 0, 0, 0, 'no'],
         [1, 0, 0, 1, 0, 'no'],
         [1, 1, 0, 0, 0, 'yes'],
         [1, 1, 1, 0, 0, 'no'],
         [1, 1, 1, 1, 0, 'no'],
         [0, 0, 0, 0, 1, 'no'],
         [1, 0, 0, 0, 1, 'no'],
         [1, 1, 0, 0, 1, 'no'],
         [1, 1, 1, 0, 1, 'no'],
         [1, 1, 1, 1, 1, 'no']
         ]

labels = ['leave', 'sickleave', 'over', 'late', 'kuanggong']
labels_feat = {"late": {0: "no", 1: "yes"},
               "leave": {0: "no", 1: "yes"},
               "sickleave": {0: "no", 1: "yes"},
               "over": {0: "no", 1: "yes"},
               "kuanggong": {0: "no", 1: "yes"}}

# datas = [[0, 1, 1, '1'],
#          [0, 1, 2, '2'],
#          [0, 1, 3, '3'],
#          [0, 2, 1, '2'],
#          [0, 2, 2, '3'],
#          [0, 2, 3, '4'],
#          [0, 3, 1, '3'],
#          [0, 3, 2, '4'],
#          [0, 3, 3, '5'],
#          [1, 1, 1, '5'],
#          [1, 2, 2, '5'],
#          [1, 3, 3, '5']]
# labels = ["tool", "profit", "satistied"]
# labels_feat = {"tool": {0: "no", 1: "yes"},
#                "profit": {0: "no", 1: "low", 2: "high", 3: "veryHigh"},
#                "satistied": {0: "no", 1: "low", 2: "high", 3: "veryHigh"}}

def get_Data():
    return datas, labels, labels_feat