# -*- coding:utf-8 -*-

from math import log
from ID3_ import id3_datas

class Algorithm(object):
    def __init__(self):
        # 最佳增益初始化,最佳特征初始化,最佳相应特征数据字典初始化
        self.grain_best = 0.0
        self.feat_best = -1
        self.label_best = ''
        self.feat_data_best = {}

    # 计算期望信息
    def algorithm_ExpInfo(self, datas):
        # 期望信息 初始化
        exp_info = 0.0
        # 创建字典,统计每个特征,不同类所出现次数
        label_count = {}
        # 计算样本总数
        num_Sample = len(datas)
        # 将类进行划分统计
        for feat in datas:
            label = feat[-1]
            if label not in label_count:
                label_count[label] = 0
            label_count[label] += 1
        # 计算期望信息
        for label in label_count:
            probe = float(label_count[label])/num_Sample
            exp_info -= probe * log(probe, 2)
        return exp_info

    # 给指定特征划分数据
    def split_Feature(self, datas, axis, feat_):
        # 初始化数据
        data = []
        # 排除指定特征,划分出其他数据
        for feat in datas:
            if feat[axis] == feat_:
                data_reset = feat[:axis]
                data_reset.extend(feat[axis+1:])
                data.append(data_reset)
        return data

    # 遍历数据集,判断划分方式
    def run(self, datas, labels,label_feat):
        self.grain_best = 0.0
        self.feat_best = -1
        # 计算根部期望信息
        base_expInfo = self.algorithm_ExpInfo(datas)
        # 获取特征个数
        num_feat = len(datas[0])-1
        for i in range(num_feat):
            # 对特征类别进行初步统计,并去重
            feat_list = [feat[i] for feat in datas]
            feat_set = set(feat_list)
            # 熵值初始化
            entropy = 0.0
            # 初始化特征数据
            feat_data = {}
            # 对特征类别划分数据,并进行统计,计算期望信息
            for feat_ in feat_set:
                # 子集期望信息初始化
                exp_info_sub = 0.0
                data = self.split_Feature(datas, i, feat_)
                # print data
                # 收集特征数据
                feat_data[label_feat[labels[i]][feat_]] = data
                # 计算子集期望信息
                exp_info_sub = self.algorithm_ExpInfo(data)
                # 计算熵值
                probe = float(len(data)) / len(datas)
                entropy += probe * exp_info_sub
            # 计算信息增益
            grain = base_expInfo - entropy
            # print feat_data
            # print i, grain
            # 刷新最佳增益
            if grain > self.grain_best:
                self.grain_best = grain
                self.feat_best = i
                self.feat_data_best = feat_data
        # print labels, self.feat_best, self.feat_data_best
        self.label_best = labels[self.feat_best]
        return self.feat_best, self.label_best, self.grain_best, self.feat_data_best