import re

array = {}

def extractNGrams(words):
    ngrams = []
    for i in range(2, 8):
        for j in range(0, len(words) - i + 1):
            ngram = ""
            for k in range(j, j + i):
                ngram += words[k] + " "
            ngrams.append(ngram)
    return ngrams

def compute(filename):
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

compute('text')
print(array)