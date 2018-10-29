import sys
import random
from histogram import countWords, countWordsArray


def arrayToString(*array):
    """takes in an array and returns the a string of the elements separated by spaces"""
    string = ""
    for elem in array:
        string += elem + " "
    return string

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
    args = sys.argv[1:]
    new = []
    for arg in args:
        new.append(str(arg))
    x = 1000
    myArr = []
    while x > 0:
        myArr.append(weightedWord(countWords(new)))
        x -= 1
    myArr = sortArray(myArr)
    print(countWordsArray(myArr))


"""➜  tweet-generator git:(master) ✗ python3 stochastic.py hey tutu tut tut tut hehehehehe
[['hehehehehe', 119], ['hey', 108], ['tut', 656], ['tutu', 117]]"""
