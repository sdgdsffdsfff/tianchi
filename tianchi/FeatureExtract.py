# encoding = utf-8
__author__ = 'kaiserding'

import csv

browseMap = {}
collectMap = {}
cartMap = {}
buyMap = {}
resultMap = {}
keySet = set()
with open('/Users/kaiserding/kaiser/tianchi/user.csv') as myFile:
    lines = csv.reader(myFile)

    for line in lines:
        userid = line[0]
        itemid = line[1]
        action = line[2]
        timeStr = line[5]
        dateStr = timeStr.split(" ")[0]
        month = int(dateStr.split("-")[1])
        day = int(dateStr.split("-")[2])
        # print month, day
        key = userid + "+" + itemid
        keySet.add(key)
        if month == 12 and day == 18:
            if action == "1":
                browseMap[key] = 1
            elif action == "2":
                collectMap[key] = 1
            elif action == "3":
                cartMap[key] = 1
            elif action == "4":
                buyMap[key] = 1
        else:
            if action == "4":
                resultMap[key] = 1

myFile.close()
print cartMap.__sizeof__()

# output = open("/Users/kaiserding/kaiser/tianchi/feature_extract.txt", "w")
#
# for key in keySet:
#     isBrowse = "0"
#     isCollect = "0"
#     isCart = "0"
#     isBuy = "0"
#     result = "0"
#     if browseMap.has_key(key):
#         isBrowse = "1"
#     if collectMap.has_key(key):
#         isCollect = "1"
#     if cartMap.has_key(key):
#         isCart = "1"
#     if buyMap.has_key(key):
#         isBuy = "1"
#     if resultMap.has_key(key):
#         result = "1"
#     keySplits = key.split("+")
#     # print (keySplits[0], keySplits[1], isBrowse, isCollect, isCart, isBuy, result)
#     output.writelines(keySplits[0] + "\t" + keySplits[1] + "\t" + isBrowse + "\t" +
#                       isCollect + "\t" + isCart + "\t" + isBuy + "\t" + result + "\n")
# output.close()




