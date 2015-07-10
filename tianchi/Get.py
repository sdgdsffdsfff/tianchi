__author__ = 'kaiserding'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# projectFile = open("/home/yeqing/project.txt")
# hash_class_to_projects = {}
# hash_id_to_class = {}
# for line in projectFile:
#     splits = line.split("\t")
#     projectID = splits[0]
#     projectClass = splits[2]
#     hash_id_to_class[projectID] = projectClass
#     if projectID not in hash_class_to_projects:
#         hash_class_to_projects[projectClass] = [projectID]
#     else:
#         project_list = hash_class_to_projects.get(projectClass)
#         project_list.append(projectID)
#         hash_class_to_projects[projectClass] = project_list

targetIDFile = open("/home/yeqing/kaiser/targetIDs.txt")

targetIDSet = set()
for line in targetIDFile:
    targetIDSet.add(line.strip())

targetIDFile.close()
# projectClass = hash_id_to_class.get(targetID)

# statisFile = open("/home/yeqing/statistic.txt")
# userSet = set()
# for line in statisFile:
#     if targetID == splits[1]:
#         userSet.add(splits[0])
# print(targetID)
# print(userSet.__sizeof__())
# statisFile.close()
#
#
# resultFile = open("/home/yeqing/result.txt", "w")
# statisFile = open("/home/yeqing/statistic.txt")
# for line in statisFile:
#     splits = line.strip().split("\t")
#     if targetID == splits[1] and splits[14] > 0:
#         resultFile.write(line)
#     elif targetID != splits[1] and splits[0] in userSet and projectClass == splits[8] and splits[14] > 0:
#         for i in range(14, 20):
#             splits[i] = 0
#         splits[1] = targetID
#         resultFile.write("\t".join(splits))
# resultFile.close()
# statisFile.close()
trainFile = open("/home/yeqing/kaiser/my_train.txt", "w")
testFile = open("/home/yeqing/kaiser/my_test.txt", "w")
normalFile = open("/home/yeqing/kaiser/last.txt")
for line in normalFile:
    splits = line.strip().split("\t")
    if splits[1] in targetIDSet:
        testFile.write(line)
    else:
        trainFile.write(line)
trainFile.close()
testFile.close()
normalFile.close()



