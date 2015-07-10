# coding=utf-8
# encoding=gbk
__author__ = 'kaiserding'
import sys
reload(sys)
# sys.setdefaultencoding('gbk')
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())

str = "哈"
str2 = u"哈"
print str2
print(len(str2))
x = str.decode("utf-8")
file = open("/Users/kaiserding/PycharmProjects/tianchi/xx", 'w')
file.write(x)
file.close()


# file = open("/Users/kaiserding/PycharmProjects/tianchi/xx")
# str = file.read()
# file.close()
# print(str)
# print(repr(str))
# print(repr(str.decode("gbk").encode("utf-8")))

