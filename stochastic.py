import sys
import random
from histogram import countWords, countWordsArray


def randomWord(histogram):
    """takes in a histogram in the form of a dictionary:

    {words : #ofAppearancesInText}

    turns the keys of the dictionary into an array
    returns a random entry from that array of keys"""
    histogram = list(histogram.keys())
    #return histogram
    return str(histogram[random.randint(0, len(histogram)-1)])

def sortArray(array):
    """takes in an array and sorts it, returning the sorted array"""
    return sorted(array)


def weightedWord(histogram):
    """takes in a dictionary histogram. splits the dictionary into two arrays,
    one of keys and the other: values.
    instantiates an empty dictionary called myDict
    cycles through the array of values
    if the value is not in myDict adds the value to the dictionary
    and the key as the first element of an array, for example:

    myDict[1] = ["Boy", "play"]

    THE ABOVE FUNCTIONAILITY HAS BEEN MOVED FROM THIS FILE TO histogram.py INTO THE FUNCTION 'keysAsValues()''

    for each time a new dictionary key is entered (which comes from the valueshistogram array)
    the value is checked against the highest_freq, and sets the highest_freq to the value

    'chance', initiate a random int between 0 and the length of the array of histogramValues

    sort the array of histogram values

    cycle through the array histogramValues with a for loop.
    if the value divided by length of the array histogramValues
    is greater than or equal to the chance variable
    return a random entry from that key in the myDict dictionary

    """
    myDict = {}
    histogramKeys = list(histogram.keys())
    histogramValues = list(histogram.values())
    highest_freq = 0
    for i, value in enumerate(histogramValues):
        if value not in myDict:
            myDict[value] = [histogramKeys[i]]
            if value > highest_freq:
                highest_freq = value
        else:
            myDict[value].append(histogramKeys[i])
        #if value > highest_freq:
        #    highest_freq = value
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
    print(keysAsValues(countWords(new)))
    #x = 1000
    #myArr = []
    #while x > 0:
    #    myArr.append(weightedWord(countWords(new)))
    #    x -= 1
    #myArr = sortArray(myArr)
    #print("\nThe program has run 1000 times and this is how many times each word was picked: \n ")
    #print(countWordsArray(myArr))


"""
➜  tweet-generator git:(master) ✗ python3 stochastic.py hey hey hey hey hey hey ho ho ho ho ho ho ho ho no no no no no no no jajajajaja jajajajaj hehe hehe he he he hehe
he

The program has run 1000 times and this is how many times each word was picked:

[['he', 135], ['hehe', 112], ['hehehe', 48], ['hey', 371], ['ho', 125], ['jajajajaj', 40], ['jajajajaja', 50], ['no', 119]]
"""
