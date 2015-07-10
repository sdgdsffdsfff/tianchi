# encoding = utf-8
__author__ = 'kaiserding'

import numpy
from sklearn import linear_model
from sklearn import metrics
import csv

trainData = numpy.loadtxt('/Users/kaiserding/kaiser/tianchi/new_data/train_3.txt',
                          delimiter="\t")
testData = numpy.loadtxt('/Users/kaiserding/kaiser/tianchi/new_data/predict_2.txt',
                         delimiter="\t")

X = trainData[:, 3:-1]
y = trainData[:, -1]
X_test = testData[:, 3:]
# y_test = testData[:, -1]
logreg = linear_model.LogisticRegression()

print(logreg.get_params())
logreg.fit(X, y)
pred = logreg.predict(X_test)


with open('/Users/kaiserding/kaiser/tianchi/result.csv', 'w') as myFile:
    myWriter = csv.writer(myFile)
    count = 0
    for i in range(0, pred.size - 1):
        if pred[i] == 1:
            print(str(testData[i][0])[0:-2], str(testData[i][1])[0:-2])
            myWriter.writerow([str(testData[i][0])[0:-2], str(testData[i][1])[0:-2]])
            count += 1
    print(count)
myFile.close()
#本地测试
# count = 0
# for i in range(0, pred.size - 1):
#     if pred[i] == 1:
#         count += 1
# print(count)
# m_precision = metrics.precision_score(y_test, pred)
# m_recall = metrics.recall_score(y_test, pred)
# print 'precision:{0:.3f}'.format(m_precision)
# print 'recall:{0:0.3f}'.format(m_recall)


