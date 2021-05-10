import numpy
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing


allElectronicsData = open('D:\pythonProject\douban/AllElectronics.csv', 'rt')#rt模式下，python在读取文本时会自动把\r\n转换成\n，文本文件用二进制读取用‘rt’
reader = csv.reader(allElectronicsData) #按行读取内容
headers = next(reader)#数据的标题  RID,age,income,student,credit_rating,class_buys_computer

#print(headers)

featureList = []#装特征值
labelList = []#装结果标签

for row in reader:
    labelList.append(row[len(row)-1])#将每一行的最后一个值，也就是标签值 存到labelList中
    rowDict = {} #创建字典
    for i in range(1, len(row)-1):#遍历该行的特征值
        rowDict[headers[i]] = row[i]#将特征值对应的 key 和 数值
    featureList.append(rowDict)


# Vetorize features
print(featureList)
vec = DictVectorizer()#字典特征提取器
dummyX = vec.fit_transform(featureList) .toarray()
print(vec.get_feature_names())
print("dummyX: " + str(dummyX))


# vectorize class labels
print("labelList: " + str(labelList))
lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY: " + str(dummyY))


# Using decision tree for classification
clf = tree.DecisionTreeClassifier(criterion='entropy')#criterion='entropy'指的是度量标准采用 信息熵 （information gain）
clf = clf.fit(dummyX, dummyY) #将数据格式转换好的 特征值和标签值 进行建模
#print("clf: " + str(clf))


# Visualize model
with open("allElectronicInformationGainOri.dot", 'w') as f:#dot -Tpdf allElectronicInformationGainOri.dot -o outpu.pdf
    f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

#accuracy
#print("样本分类的准确度:",clf.score(dummyX,dummyY)*100,"%")


#单个predict
oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))

newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
newRowX[4] = 0
print("newRowX: " + str(newRowX))

predictedY = clf.predict(numpy.array(newRowX).reshape(1,-1))
print("predictedY: " + str(predictedY))
print("-"*20)
print("-"*20)

#多个predict
allElectronicsData2 = open('D:\pythonProject\douban/AllElectronics pred.csv', 'rt')#rt模式下，python在读取文本时会自动把\r\n转换成\n，文本文件用二进制读取用‘rt’
reader2 = csv.reader(allElectronicsData2) #按行读取内容
headers2 = next(reader2)#数据的标题  RID,age,income,student,credit_rating,class_buys_computer


featureList2 = []
labelList2 = []
for r in reader2:
    labelList2.append(r[len(r) - 1])
    rowDict2 = {} #创建字典
    for i in range(1, len(r)-1):#遍历该行的特征值
        rowDict2[headers2[i]] = r[i]#将特征值对应的 key 和 数值
    featureList2.append(rowDict2)


# Vetorize features
print(featureList2)
dummyX2 = vec.fit_transform(featureList2) .toarray()
print(vec.get_feature_names())
print("dummyX2: " + str(dummyX2))


# vectorize class labels
print("labelList2: " + str(labelList2))
lb2 = preprocessing.LabelBinarizer()
dummyY2 = lb2.fit_transform(labelList2)
print("dummyY2: " + str(dummyY2))#打印测试集的正确结果


predict2=[]
for j in range(0,len(dummyX2)):
    pre=clf.predict(numpy.array(dummyX2[j]).reshape(1,-1))
    predict2.append(int(pre))
print("predictY2:",predict2)#打印测试集的预测结果


print("测试分类的准确度:",clf.score(dummyX2,dummyY2)*100,"%")