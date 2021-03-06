import csv
import random
import math
import operator

#加载数据集
def loadDataset(filename, split, trainingSet = [], testSet = []):
    with open(filename, 'rt') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

#计算出 点与点之间的距离
def euclideanDistance(instance1, instance2, length):#length表示维度
    distance = 0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]), 2)
    return math.sqrt(distance)

#返回k个最近的邻居
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        #testinstance
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
        #distances.append(dist)
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
        return neighbors

#根据k个邻居 来判断出结果
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)#按降序排列
    return sortedVotes[0][0]

#判断准确率
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet)))*100.0


def main():
    #prepare data
    trainingSet = []
    testSet = []
    split = 0.5 #数据的一半为trainingSet，一半为testSet
    loadDataset('irisdata.txt', split, trainingSet, testSet)
    print('Train set: ' + str(len(trainingSet)))
    print('Test set: ' + str(len(testSet)))
    #generate predictions
    predictions = []
    k = 3
    for i in range(len(testSet)):
        # trainingsettrainingSet[x]
        neighbors = getNeighbors(trainingSet, testSet[i], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('>预测值=' + str(result) + ', 真实值=' + str(testSet[i][-1]))
    accuracy = getAccuracy(testSet, predictions)
    print('Accuracy: ' + str(accuracy) + '%')


main()