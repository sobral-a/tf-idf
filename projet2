#!/usr/bin/env python3 
import re
import math
import sys

array = {}
n = 0

def extractNGrams(words):
    ngrams = []
    for i in range(2, 8):
        for j in range(0, len(words) - i + 1):
            ngram = ""
            for k in range(j, j + i):
                if k != j + i - 1:
                    ngram += words[k] + " "
                else:
                    ngram += words[k]
            ngrams.append(ngram)
    return ngrams

def compute(filename):
    global n
    n += 1
    text = open(filename)
    textWords = re.findall(r"[\w']+", text.read())
    words = extractNGrams(textWords)
    for w in words:
        if w in array:
            array[w]["occurences"] += 1
            if filename not in array[w]["textes"]:
                array[w]["textes"].append(filename)
        else:
            array[w] = { "occurences" : 1, "textes": [filename] }
    
def computeTFIDF():
    maxOccurences = max(ngram["occurences"] for ngram in array.values())
    results = {}
    for key, value in array.items():
        tf = float(value["occurences"] / maxOccurences)
        idf = float(math.log(n / len(value["textes"])) + 1)
        tfidf = tf * idf
        results[key] = tfidf
    return results

def reverse(l):
    return [l.pop() for _ in range(len(l))]

def start():
    args = sys.argv[1:]
    if len(args) < 1:
        print("You have to provide at least one text.")
        return
    for arg in args:
        compute(arg)
    results = computeTFIDF()
    resultArray = sorted(results.items(), key=lambda x:x[1])
    resultArray = reverse(resultArray)
    for i in range (0, 10):
        print("{0} => {1}".format(resultArray[i][0], resultArray[i][1]))

start()