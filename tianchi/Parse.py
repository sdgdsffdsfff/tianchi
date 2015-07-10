# encoding = utf-8
# coding=utf-8
__author__ = 'kaiserding'
import json
import re
import argparse
import sys
from HTMLParser import HTMLParser

reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser(description="corpusParser")
parser.add_argument('-i', type=str, default='', help='')
parser.add_argument('-o', type=str, default='', help='')
args = parser.parse_args()

def Parse():
    if args.f == '':
        return ''
    if args.o == '':
        return ''
    outputFile = open(args.o, "w")
    inputFile = open(args.f)
    for line in inputFile.readlines():
        splits = line.split("\t")
        description = splits[2]
        subdescription = splits[3]
        new_des = ''
        new_sub = ''
        if description != '':
            new_des = strip_tags(description).replace(' ', '')
        if subdescription != '':
            new_sub = strip_tags(parseJson(subdescription.replace("\\\\", "\\").replace("\\n", ''))).replace(' ', '').replace("\t", '')
        if new_des == '' and new_sub == '':
            continue
        outputFile.write(splits[0] + "\t" + splits[1].replace(' ', '') + new_des + new_sub + "\n")
    inputFile.close()
    outputFile.close()

def testParse(line):
    splits = line.split("\t")
    description = splits[2]
    subdescription = splits[3]
    new_des = strip_tags(description).replace(' ', '')
    new_sub = strip_tags(parseJson(subdescription.replace("\\\\", "\\").replace("\\n", ''))).replace(' ', '').replace(
        "\t", '')
    return splits[0] + "\t" + splits[1] + new_des + new_sub


def parseJson(str):
    jsonObject = json.loads(str)
    return jsonObject['dealdesc'] + jsonObject['bizinfo']


def stripTagSimple(htmlStr):
    dr = re.compile(r'</?\w+[^>]*>', re.S)
    htmlStr = re.sub(dr, '', htmlStr)
    return htmlStr


def strip_tags(htmlStr):
    htmlStr = htmlStr.strip()
    htmlStr = htmlStr.strip("\n")
    result = []
    parser = HTMLParser()
    parser.handle_data = result.append
    parser.feed(htmlStr)
    parser.close()
    return ''.join(result)


if __name__ == '__main__':
    # str = '104900	酒谷和风料理 美食 日韩菜 日本菜以下7选1 葱香牛肉盖饭 鸡肉蛋饭 牛肉蛋饭 猪扒蛋饭 咖喱牛肉饭 咖喱鸡肉饭 咖喱猪扒饭	<!--项目介绍-->        <p class="standard-bar" >美团实拍</p>            <ul class="list">                <li>                    <strong>葱香牛肉盖饭</strong>                ：味浓肉嫩，焦香郁浓，葱味宜人。            </li>            </ul>                    <img  data-height="266" src="http://p0.meituan.net/deal/201301/17/140649_1979347.jpg" alt="美团图" class="standard-image">            <ul class="list">                <li>                    <strong>鸡肉蛋饭</strong>                ：美味的鸡肉，配上香喷喷的米饭，十分开胃诱人。            </li>            </ul>                    <img  data-height="266" src="http://p0.meituan.net/deal/201301/17/140645_8713768.jpg" alt="美团图" class="standard-image">            <ul class="list">                <li>                    <strong>牛肉蛋饭</strong>                ：肥牛肉片厚薄适中，肥瘦比例口感甚佳，口感独特。            </li>            </ul>                    <img  data-height="266" src="http://p1.meituan.net/deal/201301/17/140648_2708349.jpg" alt="美团图" class="standard-image">            <ul class="list">                <li>                    <strong>猪扒蛋饭</strong>                ：因有了酱汁的调味，猪肉肥而不腻，不仅烹调手法独特，口感和味道也充满异国情调，是值得一试的开胃菜式！            </li>            </ul>                    <img  data-height="266" src="http://p0.meituan.net/deal/201301/17/140647_5279452.jpg" alt="美团图" class="standard-image">            <ul class="list">                <li>                    <strong>咖喱牛肉饭</strong>                ：浓郁的咖喱味遇上嫩滑的牛肉，口感十足。             </li>            </ul>                    <img  data-height="266" src="http://p1.meituan.net/deal/201301/17/140645_7952019.jpg" alt="美团图" class="standard-image">            <ul class="list">                <li>                    <strong>咖喱猪扒饭</strong>                ：嫩滑的蛋、肉质鲜嫩的猪扒搭配而成的，尝上一口，齿颊留香，瞬间刺激着整个味蕾，让人回味无穷。            </li>            </ul>                    <img  data-height="266" src="http://p1.meituan.net/deal/201301/17/140645_8363866.jpg" alt="美团图" class="standard-image">            <ul class="list">                <li>                    <strong>味增汤</strong>                ：一碗汤的味道，是回忆的味道，还记得上次一起喝汤的他吗？            </li>            </ul>                    <img  data-height="266" src="http://p0.meituan.net/deal/201301/17/140647_5554797.jpg" alt="美团图" class="standard-image">            <ul class="list">                <li>                    <strong>可升级套餐</strong>            </li>            </ul>            <ul class="list">                <li>                    <strong>青花鱼定食</strong>            </li>            </ul>                    <img  data-height="266" src="http://p1.meituan.net/deal/201301/17/140648_3762352.jpg" alt="美团图" class="standard-image">            <ul class="list">                <li>                    <strong>猪肉生姜定食</strong>            </li>            </ul>                    <img  data-height="266" src="http://p1.meituan.net/deal/201301/17/140647_8359566.jpg" alt="美团图" class="standard-image">    <!--商家介绍-->    <!--bizIntroductStart-->            <p class="standard-bar" >酒谷和风料理</p>            <img  data-height="266" src="http://p0.meituan.net/deal/201301/17/140644_9921898.jpg" alt="美团图" class="standard-image">                <p>酒谷和风料理位于椒江区康平路348号，店面典雅精致，装饰温馨，我们会根据季节变化和餐饮的流行趋势，适时推出不同菜肴。菜式丰富，色泽亮丽，口感极佳，令人难以忘怀。我们提倡“自然的、清新的、新鲜的、清淡的、健康的”饮食观念。特色推荐： “刺身船”是高档的贵族食品，凡盛大庆典或宴请宾客，“刺身船”作为一道久负盛名的菜，总是以大菜的头牌身份出现。</p>                    <img  data-height="266" src="http://p0.meituan.net/deal/201301/17/140648_3998157.jpg" alt="美团图" class="standard-image">                    <img  data-height="266" src="http://p1.meituan.net/deal/201301/17/140646_5393514.jpg" alt="美团图" class="standard-image">                    <img  data-height="266" src="http://p0.meituan.net/deal/201301/17/140646_8453620.jpg" alt="美团图" class="standard-image">                    <img  data-height="266" src="http://p1.meituan.net/deal/201301/17/140646_5886210.jpg" alt="美团图" class="standard-image">                    <img  data-height="266" src="http://p0.meituan.net/deal/201301/17/140645_3636147.jpg" alt="美团图" class="standard-image">    <!--bizIntroductEnd-->	{"dealdesc":"<!--\\u9879\\u76ee\\u4ecb\\u7ecd-->\\n        <p class=\\"standard-bar\\" >\\u7f8e\\u56e2\\u5b9e\\u62cd<\\/p>\\n            <ul class=\\"list\\">\\n                <li>\\n                    <strong>\\u8471\\u9999\\u725b\\u8089\\u76d6\\u996d<\\/strong>\\n                \\uff1a\\u5473\\u6d53\\u8089\\u5ae9\\uff0c\\u7126\\u9999\\u90c1\\u6d53\\uff0c\\u8471\\u5473\\u5b9c\\u4eba\\u3002\\t\\n\\n            <\\/li>\\n            <\\/ul>\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p0.meituan.net\\/deal\\/201301\\/17\\/140649_1979347.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n            <ul class=\\"list\\">\\n                <li>\\n                    <strong>\\u9e21\\u8089\\u86cb\\u996d<\\/strong>\\n                \\uff1a\\u7f8e\\u5473\\u7684\\u9e21\\u8089\\uff0c\\u914d\\u4e0a\\u9999\\u55b7\\u55b7\\u7684\\u7c73\\u996d\\uff0c\\u5341\\u5206\\u5f00\\u80c3\\u8bf1\\u4eba\\u3002\\t\\n\\n            <\\/li>\\n            <\\/ul>\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p0.meituan.net\\/deal\\/201301\\/17\\/140645_8713768.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n            <ul class=\\"list\\">\\n                <li>\\n                    <strong>\\u725b\\u8089\\u86cb\\u996d<\\/strong>\\n                \\uff1a\\u80a5\\u725b\\u8089\\u7247\\u539a\\u8584\\u9002\\u4e2d\\uff0c\\u80a5\\u7626\\u6bd4\\u4f8b\\u53e3\\u611f\\u751a\\u4f73\\uff0c\\u53e3\\u611f\\u72ec\\u7279\\u3002\\t\\n\\n            <\\/li>\\n            <\\/ul>\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p1.meituan.net\\/deal\\/201301\\/17\\/140648_2708349.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n            <ul class=\\"list\\">\\n                <li>\\n                    <strong>\\u732a\\u6252\\u86cb\\u996d<\\/strong>\\n                \\uff1a\\u56e0\\u6709\\u4e86\\u9171\\u6c41\\u7684\\u8c03\\u5473\\uff0c\\u732a\\u8089\\u80a5\\u800c\\u4e0d\\u817b\\uff0c\\u4e0d\\u4ec5\\u70f9\\u8c03\\u624b\\u6cd5\\u72ec\\u7279\\uff0c\\u53e3\\u611f\\u548c\\u5473\\u9053\\u4e5f\\u5145\\u6ee1\\u5f02\\u56fd\\u60c5\\u8c03\\uff0c\\u662f\\u503c\\u5f97\\u4e00\\u8bd5\\u7684\\u5f00\\u80c3\\u83dc\\u5f0f\\uff01\\t\\n\\n            <\\/li>\\n            <\\/ul>\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p0.meituan.net\\/deal\\/201301\\/17\\/140647_5279452.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n            <ul class=\\"list\\">\\n                <li>\\n                    <strong>\\u5496\\u55b1\\u725b\\u8089\\u996d<\\/strong>\\n                \\uff1a\\u6d53\\u90c1\\u7684\\u5496\\u55b1\\u5473\\u9047\\u4e0a\\u5ae9\\u6ed1\\u7684\\u725b\\u8089\\uff0c\\u53e3\\u611f\\u5341\\u8db3\\u3002 \\t\\n\\n            <\\/li>\\n            <\\/ul>\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p1.meituan.net\\/deal\\/201301\\/17\\/140645_7952019.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n            <ul class=\\"list\\">\\n                <li>\\n                    <strong>\\u5496\\u55b1\\u732a\\u6252\\u996d<\\/strong>\\n                \\uff1a\\u5ae9\\u6ed1\\u7684\\u86cb\\u3001\\u8089\\u8d28\\u9c9c\\u5ae9\\u7684\\u732a\\u6252\\u642d\\u914d\\u800c\\u6210\\u7684\\uff0c\\u5c1d\\u4e0a\\u4e00\\u53e3\\uff0c\\u9f7f\\u988a\\u7559\\u9999\\uff0c\\u77ac\\u95f4\\u523a\\u6fc0\\u7740\\u6574\\u4e2a\\u5473\\u857e\\uff0c\\u8ba9\\u4eba\\u56de\\u5473\\u65e0\\u7a77\\u3002\\t\\n\\n            <\\/li>\\n            <\\/ul>\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p1.meituan.net\\/deal\\/201301\\/17\\/140645_8363866.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n            <ul class=\\"list\\">\\n                <li>\\n                    <strong>\\u5473\\u589e\\u6c64<\\/strong>\\n                \\uff1a\\u4e00\\u7897\\u6c64\\u7684\\u5473\\u9053\\uff0c\\u662f\\u56de\\u5fc6\\u7684\\u5473\\u9053\\uff0c\\u8fd8\\u8bb0\\u5f97\\u4e0a\\u6b21\\u4e00\\u8d77\\u559d\\u6c64\\u7684\\u4ed6\\u5417\\uff1f\\n            <\\/li>\\n            <\\/ul>\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p0.meituan.net\\/deal\\/201301\\/17\\/140647_5554797.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n            <ul class=\\"list\\">\\n                <li>\\n                    <strong>\\u53ef\\u5347\\u7ea7\\u5957\\u9910<\\/strong>\\n            <\\/li>\\n            <\\/ul>\\n            <ul class=\\"list\\">\\n                <li>\\n                    <strong>\\u9752\\u82b1\\u9c7c\\u5b9a\\u98df<\\/strong>\\n            <\\/li>\\n            <\\/ul>\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p1.meituan.net\\/deal\\/201301\\/17\\/140648_3762352.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n            <ul class=\\"list\\">\\n                <li>\\n                    <strong>\\u732a\\u8089\\u751f\\u59dc\\u5b9a\\u98df<\\/strong>\\n            <\\/li>\\n            <\\/ul>\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p1.meituan.net\\/deal\\/201301\\/17\\/140647_8359566.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n    <!--\\u5546\\u5bb6\\u4ecb\\u7ecd-->","bizinfo":"<p class=\\"standard-bar\\" >\\u9152\\u8c37\\u548c\\u98ce\\u6599\\u7406<\\/p>\\n            <img  data-height=\\"266\\" src=\\"http:\\/\\/p0.meituan.net\\/deal\\/201301\\/17\\/140644_9921898.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n                <p>\\u9152\\u8c37\\u548c\\u98ce\\u6599\\u7406\\u4f4d\\u4e8e\\u6912\\u6c5f\\u533a\\u5eb7\\u5e73\\u8def348\\u53f7\\uff0c\\u5e97\\u9762\\u5178\\u96c5\\u7cbe\\u81f4\\uff0c\\u88c5\\u9970\\u6e29\\u99a8\\uff0c\\u6211\\u4eec\\u4f1a\\u6839\\u636e\\u5b63\\u8282\\u53d8\\u5316\\u548c\\u9910\\u996e\\u7684\\u6d41\\u884c\\u8d8b\\u52bf\\uff0c\\u9002\\u65f6\\u63a8\\u51fa\\u4e0d\\u540c\\u83dc\\u80b4\\u3002\\u83dc\\u5f0f\\u4e30\\u5bcc\\uff0c\\u8272\\u6cfd\\u4eae\\u4e3d\\uff0c\\u53e3\\u611f\\u6781\\u4f73\\uff0c\\u4ee4\\u4eba\\u96be\\u4ee5\\u5fd8\\u6000\\u3002\\u6211\\u4eec\\u63d0\\u5021\\u201c\\u81ea\\u7136\\u7684\\u3001\\u6e05\\u65b0\\u7684\\u3001\\u65b0\\u9c9c\\u7684\\u3001\\u6e05\\u6de1\\u7684\\u3001\\u5065\\u5eb7\\u7684\\u201d\\u996e\\u98df\\u89c2\\u5ff5\\u3002\\n\\u7279\\u8272\\u63a8\\u8350\\uff1a \\u201c\\u523a\\u8eab\\u8239\\u201d\\u662f\\u9ad8\\u6863\\u7684\\u8d35\\u65cf\\u98df\\u54c1\\uff0c\\u51e1\\u76db\\u5927\\u5e86\\u5178\\u6216\\u5bb4\\u8bf7\\u5bbe\\u5ba2\\uff0c\\u201c\\u523a\\u8eab\\u8239\\u201d\\u4f5c\\u4e3a\\u4e00\\u9053\\u4e45\\u8d1f\\u76db\\u540d\\u7684\\u83dc\\uff0c\\u603b\\u662f\\u4ee5\\u5927\\u83dc\\u7684\\u5934\\u724c\\u8eab\\u4efd\\u51fa\\u73b0\\u3002<\\/p>\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p0.meituan.net\\/deal\\/201301\\/17\\/140648_3998157.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p1.meituan.net\\/deal\\/201301\\/17\\/140646_5393514.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p0.meituan.net\\/deal\\/201301\\/17\\/140646_8453620.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p1.meituan.net\\/deal\\/201301\\/17\\/140646_5886210.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">\\n                    <img  data-height=\\"266\\" src=\\"http:\\/\\/p0.meituan.net\\/deal\\/201301\\/17\\/140645_3636147.jpg\\" alt=\\"\\u7f8e\\u56e2\\u56fe\\" class=\\"standard-image\\">"}'
    # print(testParse(str))
    Parse()











