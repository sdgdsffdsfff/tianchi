# coding=utf-8
__author__ = 'kaiserding'

import jieba
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# print("Default Mode:" + "/".join(seg_list))
inputFile = open("/Users/kaiserding/PycharmProjects/segment/Resources/z2")
outputFile = open("/Users/kaiserding/PycharmProjects/segment/Resources/seg2.txt", "w")
for line in inputFile:
    splits = line.split("\t")
    seg_list = jieba.cut(splits[1], cut_all=False)
    outputFile.write(splits[0] + "\t" + "^".join(seg_list))
inputFile.close()
outputFile.close()

