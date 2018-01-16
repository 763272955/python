# -*- coding:utf-8 -*-

from math import log
import operator

def createDataSet():
    dataSet = [[1, 3, 0, 1, 'no'],
               [1, 3, 0, 2, 'no'],
               [2, 3, 0, 1, 'yes'],
               [3, 2, 0, 1, 'yes'],
               [3, 1, 1, 1, 'yes'],
               [3, 1, 1, 2, 'no'],
               [2, 1, 1, 2, 'yes'],
               [1, 2, 0, 1, 'no'],
               [1, 1, 1, 1, 'yes'],
               [3, 2, 1, 1, 'yes'],
               [1, 2, 1, 2, 'yes'],
               [2, 2, 0, 2, 'yes'],
               [2, 3, 0, 1, 'yes'],
               [3, 2, 0, 2, 'no'],
               ]
    labels = ['age', 'salary', 'isStudent', 'credit']

    # change to discrete values
    return dataSet, labels


############计算香农熵###############
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  # 计算实例的总数
    labelCounts = {}  # 创建一个数据字典，它的key是最后把一列的数值(即标签)，value记录当前类型（即标签）出现的次数
    for featVec in dataSet:  # 遍历整个训练集
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0  # 初始化香农熵
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)  # 计算香农熵
    return shannonEnt


#########按给定的特征划分数据#########
def splitDataSet(dataSet, axis, value):  # axis表示特征的索引　　value是返回的特征值
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            # reducedFeatVec = featVec[:axis]  # 抽取除axis特征外的所有的记录的内容
            # reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(featVec[-1])
    return retDataSet


#######遍历整个数据集，选择最好的数据集划分方式########
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 4  # 获取当前实例的特征个数，一般最后一列是标签。the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)  # 计算当前实例的香农熵
    bestInfoGain = 0.0
    bestFeature = -1  # 这里初始化最佳的信息增益和最佳的特征
    for i in range(numFeatures):  # 遍历每一个特征　iterate over all the features
        featList = [example[i] for example in dataSet]  # create a list of all the examples of this feature
        uniqueVals = set(featList)  # 创建唯一的分类标签
        newEntropy = 0.0
        for value in uniqueVals:  # 计算每种划分方式的信息熵
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy  # 计算信息增益
        if (infoGain > bestInfoGain):  # 比较每个特征的信息增益，只要最好的信息增益
            bestInfoGain = infoGain  # if better than current best, set to best
            bestFeature = i
    return bestFeature, bestInfoGain  # 返回最佳划分的特征索引和信息增益


'''''该函数使用分类名称的列表，然后创建键值为classList中唯一值的数据字典。字典
对象的存储了classList中每个类标签出现的频率。最后利用operator操作键值排序字典，
并返回出现次数最多的分类名称
'''


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  # 返回所有的标签
    if classList.count(classList[0]) == len(classList):  # 当类别完全相同时则停止继续划分，直接返回该类的标签
        return classList[0]  # stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1:  # 遍历完所有的特征时，仍然不能将数据集划分成仅包含唯一类别的分组
        return majorityCnt(classList)  # 由于无法简单的返回唯一的类标签，这里就返回出现次数最多的类别作为返回值
    bestFeat, bestInfogain = chooseBestFeatureToSplit(dataSet)  # 获取最好的分类特征索引
    bestFeatLabel = labels[bestFeat]  # 获取该特征的名称
    # print bestFeatLabel
    # 这里直接使用字典变量来存储树信息，这对于绘制树形图很重要。
    myTree = {bestFeatLabel: {}}  # 当前数据集选取最好的特征存储在bestFeat中
    print myTree
    del (labels[bestFeat])  # 删除已经在选取的特征
    # print labels
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        print subLabels# copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    print myTree
    return myTree


def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else:
        classLabel = valueOfFeat
    return classLabel


def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)


import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")  # 定义文本框与箭头的格式
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def getNumLeafs(myTree):  # 获取树节点的数目
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():  # 测试节点的数据类型是不是字典，如果是则就需要递归的调用getNumLeafs()函数
        if type(secondDict[
                    key]).__name__ == 'dict':  # test to see if the nodes are dictonaires, if not they are leaf nodes
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getTreeDepth(myTree):  # 获取树节点的树的层数
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[
                    key]).__name__ == 'dict':  # test to see if the nodes are dictonaires, if not they are leaf nodes
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth


def plotNode(nodeTxt, centerPt, parentPt, nodeType):  # 绘制带箭头的注释
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',  # createPlot.ax1会提供一个绘图区
                            xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def plotMidText(cntrPt, parentPt, txtString):  # 计算父节点和子节点的中间位置，在父节点间填充文本的信息
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)


def plotTree(myTree, parentPt, nodeTxt):  # if the first key tells you what feat was split on
    numLeafs = getNumLeafs(myTree)  # 首先计算树的宽和高
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]  # the text label for this node should be this
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)  # 标记子节点的属性值
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[
                    key]).__name__ == 'dict':  # test to see if the nodes are dictonaires, if not they are leaf nodes
            plotTree(secondDict[key], cntrPt, str(key))  # recursion
        else:  # it's a leaf node print the leaf node
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


# if you do get a dictonary you know it's a tree, and the first element will be another dict
#
def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)  # no ticks
    # createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
    plotTree.totalW = float(getNumLeafs(inTree))  # c存储树的宽度
    plotTree.totalD = float(getTreeDepth(inTree))  # 存储树的深度。我们使用这两个变量计算树节点的摆放位置
    plotTree.xOff = -0.5 / plotTree.totalW;
    plotTree.yOff = 1.0;
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()

    # def createPlot():
    #     fig = plt.figure(1, facecolor='white')
    #     fig.clf()
    #     createPlot.ax1 = plt.subplot(111, frameon=False) #创建一个新图形，并清空绘图区
    #     plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)＃然后在绘图区上绘制两个代表不同类型的树节点
    #     plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    #     plt.show()


myDat, labels = createDataSet()
# print calcShannonEnt(myDat)
# print myDat

myTree = createTree(myDat, labels)
# print myTree
# print getNumLeafs(myTree)
# print getTreeDepth(myTree)
# createPlot(myTree)