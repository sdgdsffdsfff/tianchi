# encoding=utf-8
# coding=utf-8
__author__ = 'kaiserding'
import argparse
import re
parser = argparse.ArgumentParser(description="corpusParser")
parser.add_argument('-i', type=str, default='', help='')
parser.add_argument('-o', type=str, default='', help='')
args = parser.parse_args()

def load_stopwords():
    stopwords = set()
    with open('/opt/meituan/build/mining/gocode/src/topic_model/data/stopword.txt', 'r') as handle:
        for line in handle:
            stopwords.add(line.strip())
    return stopwords

def filter():
    if args.i == '':
        return ''
    if args.o == '':
        return ''
    stopwords = load_stopwords()
    inputFile = open(args.i)
    outputFile = open(args.o, "w")
    pattern = re.compile(r'^[0-9a-z.+-_%&]*$')
    for line in inputFile:
        splits = line.strip().split("\t")
        content = splits[1]
        words = content.split(" ")
        tokens = set()
        for word in words:
            if word in stopwords or pattern.match(word):
                continue
            else:
                tokens.add(word)
        outputFile.write(splits[0] + "\t" + ":".join(tokens) + "\n")
    inputFile.close()
    outputFile.close()

if __name__ == '__main__':
    filter()
