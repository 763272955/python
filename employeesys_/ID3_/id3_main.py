# -*- coding:utf-8 -*-

import id3_algorithm
import id3_datas

class ID3_Ta2Tr(object):
    def __init__(self):
        self.dddd = {}
        self.count = 0
        self.algorithm = id3_algorithm.Algorithm()

    def create_Tree(self, datas, labels, label_feat):
        class_list = [example[-1] for example in datas]
        if class_list.count(class_list[0]) == len(class_list):
            return class_list[0]
        if len(datas[0]) == 1:
            # print datas
            return
        best_feat, best_label, best_grain, best_feat_data = self.algorithm.run(datas, labels, label_feat)
        # print best_feat, best_label, best_feat_data
        tree = {best_label: {}}
        labels.remove(best_label)
        for key in best_feat_data.keys():
            subLabels = labels[:]
            tree[best_label][key] = self.create_Tree(best_feat_data[key], subLabels, label_feat)
        # print tree
        return tree

    # def run(self):
    #     datas, labels, labels_feat = id3_datas.get_Data()
    #     tree = self.create_Tree(datas, labels, labels_feat)
    #     print tree

    def run(self,datas, labels, labels_feat):
        tree = self.create_Tree(datas, labels, labels_feat)
        return tree

def train(datas, labels, labels_feat):
    obj = ID3_Ta2Tr()
    tree = obj.run(datas, labels, labels_feat)
    return str(tree)

# if __name__ == "__main__":
#     datas, labels, labels_feat = id3_datas.get_Data()
#     obj = ID3_Ta2Tr()
#     obj.run(datas, labels, labels_feat)
#     pass