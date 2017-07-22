#!/usr/bin/env python3 
import re
import math

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
        idf = float((n / len(value["textes"])) + 1)
        tfidf = tf * idf
        results[key] = tfidf
    print(results)
compute('test/text')
compute('test/text1')
computeTFIDF()