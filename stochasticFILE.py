"""

DO NOT RUN

IN PROGRESS...

MEANT TO TAKE IN A FILE AND A WORD
AND RETURN:

THE TEN MOST COMMON WORDS

HOW MANY TIMES THE WORD APPEARS

HOW MANY UNIQUE WORDS THERE ARE IN THE TEXT

AND

HOW LONG THE PROGRAM TOOK TO RUN

"""


from collections import deque
import sys
import string
import random
from histogram import countWordsDict, countWordsArray, arrayFileWords, strip_Punc, lowercaseArray, keysAsValues




def randomWord(histogram):
    histogram = list(histogram.keys())
    #return histogram
    return str(histogram[random.randint(0, len(histogram)-1)])

def sortArray(array):
    return sorted(array)

def weightedWord(histogram):
    myDict = {}
    histogramKeys = list(histogram.keys())
    histogramValues = list(histogram.values())
    highest_freq = 0
    for i, value in enumerate(histogramValues):
        if value not in myDict:
            myDict[value] = [histogramKeys[i]]
        else:
            myDict[value].append(histogramKeys[i])
        if value > highest_freq:
            highest_freq = value
    chance = random.uniform(0, highest_freq / len(histogramValues))
    histogramValues = sortArray(histogramValues)
    for value in histogramValues:
        if value / len(histogramValues) >= chance:
            return myDict[value][random.randint(0, len(myDict[value])-1)]

if __name__ == '__main__':
    file = str(sys.argv[1])
    new = lowercaseArray(strip_Punc(arrayFileWords(file)))
    myArr = keysAsValues(countWordsDict(new))
    print(myArr)
    myArr = weightedWord(countWordsDict(new))
    print(myArr)
