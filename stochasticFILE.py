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
from histogram import countWords, countWordsArray


if __name__ == '__main__':
        file = str(sys.argv[1])
        word = sys.argv[2]  #stringify here
        n = sys.argv[3]     #and here

def arrayFileWords(file):
    """opens a file, puts the words into an array,
    closes the file and returns the array of strings"""
    f = open(file, "r")
    array = f.read().split()
    f.close()
    return array

def strip_Punc(array):
    """opens an array of strings, cycles through each word and then each character
    of a word and replaces that word with an exact copy but without punctuation. returns the array."""
    punctuation = ["@" , "#" , "$" , ":", ";", "_", "*" , "}" , "[" , "{" , "]"]
    #, "," , ".", "!" , "?"] #took out single and double quotes from this array
    for i, word in enumerate(array):
        newWord = ""
        for char in word:
            if char not in punctuation:
                newWord += char
        array[i] = newWord
    return array

def lowercaseArray(array):
    """takes in an array of strings, uses a list comprehension to lowercase each letter"""
    uppercase = ["I", "\'I" , "\"I"]
    array = [x.lower() for x in array if x not in uppercase]
    return array

#def removeSpaces(array):
#    array = [array.pop(i) for i, x in enumerate(array) if x == " "]

def wordBeforeAfter(array):
    """takes in an array of strings,
    using the global variables word and n,
    looks for instances of the word in the array.
    if an instance of the word is found,
    compiles an array of n words that come before the word.
    returns an array of tuples of
    (1) instance of word,
    (2) array of n words before the instance of the searched word, and
    (3) the next word that comes after the instance of the searched word."""
    instances = []
    for i, fileWord in enumerate(array):
        if fileWord == str.lower(str(word)):
            x = i -1
            beforeWords = []
            #while x > (i - int(n) - 1): #if you want n words before word
            while x > (i - int(n)): #if you want n words after next-word
                beforeWords.append(array[x])
                x -= 1
            myTuple = (word, beforeWords, array[i+1])
            instances.append(myTuple)
    return instances

def firstOrderMarkov(arrayOfTuples):
    """takes in an array of tuples of (word, [array of words before word], next word that comes after word)
    creates a dictionary of {next word : number of instances}. splits the dictionary into a 'twin index' of two arrays: keys and values.

    "twin index" = keys[0] and values[0] reference the key and value pair of the dictionary that was 'split'.

    for each key the function prints to console what the likelihood is of that key appearing as the next word."""
    myDict = {}
    for i, instance in enumerate(arrayOfTuples):
        if instance[2] not in myDict:
            myDict[arrayOfTuples[i][2]] = 1
        else:
            myDict[arrayOfTuples[i][2]] += 1
    keys = list(myDict.keys())
    values = list(myDict.values())
    print(keys)
    print(values)

def nOrderMarkov(instances):
    """takes in an array of tuples (word, [array of n words before word], and next word),
    cycles through the array of tuples and appends the next word and the word to an array,
    and then appends the array of before words

    NEED TO EDIT DOCSTRING..."""
    arrayofArrays = []
    myDict = {}
    for i, instance in enumerate(instances):
        myArray = [] #array in "backwards" chronological order from last word (next) to first word
        myArray.append(instance[2]) #next word
        myArray.append(instance[0]) #word
        myArray+=instance[1] #array of words before word
        arrayofArrays.append(myArray)
    for array in arrayofArrays:
        if tuple(array) not in myDict:
            myDict[tuple(array)] = 1
        else:
            myDict[tuple(array)] += 1
    keys = list(myDict.keys())
    values = list(myDict.values())
    return(keys, values)

def checkChars(myTweet):
    """checks to see how many characters there are in myTweet. if there are less
    than 140 then it returns True."""
    punctuation = [".", "!" , "?"]
    counter = 0
    period = False
    for chars in myTweet:
        counter += 1
        if counter > 140 and chars in punctuation:
            period = True
        elif counter > 300:
            period = True
    if period == False:
        return True
    else:
        return False
    #and chars in punctuation:
        #    period = True
    #if period == True:
    #    return True
    #else:

myTweet = str(word)
upperRange = int(n)                          #creates variety
lowerRange = (int(n) - (int(n)//1.5))        #consider changing
if lowerRange < 1:
    lowerRange = 1
exception = True
while checkChars(myTweet) and exception:
    try:
        keysValues = nOrderMarkov(wordBeforeAfter(strip_Punc(arrayFileWords(file))))
        #keysValues = nOrderMarkov(wordBeforeAfter(strip_Punc(lowercaseArray(arrayFileWords(file)))))
        x = 0
        storeIndex = []
        for i, value in enumerate(keysValues[1]):
            if value > x:                         #right now it is just going to the highest frequency word, use herd_immunity virus_repro-style
                x = value
                storeIndex.append(i)
        word = keysValues[0][storeIndex[random.randint(((len(storeIndex)-1)//2), (len(storeIndex)-1))]][0]       #i could check to see if the word is in the sentence, would completely get rid of repeats tho...
        n = random.randint(lowerRange, upperRange)#i could check to see if the chars in the word match the up with the last 20 chars, if so use next most frequent word
        #print(len(storeIndex))
        #myTweet += str(n)                            #maybe use a queue to do first in, first out of words or chars to consistently check; repetition of the same word is killing me
        myTweet += " "
        myTweet += word
        checkChars(myTweet)
    except:
        exception = False
else:
    print(myTweet)
    #print(lowerRange)
    #print(upperRange)

#Harry potter  yes, that he had a firm called grunnings, which made the street. the dark wizard grindelwald in his work on the first sign of the
#            ^
#need to make a function that removes elements of the array that are just spaces.
#i'm guessing there are double-spaced places in the text and they're being given their own array element



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
    word = sys.argv[2]  #stringify here

    new = []
    for arg in args:
        new.append(str(arg))
    x = 1000
    myArr = []
    while x > 0:
        myArr.append(weightedWord(countWords(new)))
        x -= 1
    myArr = sortArray(myArr)
    print("\nThe program has run 1000 times and this is how many times each word was picked: \n ")
    print(countWordsArray(myArr))


"""➜  tweet-generator git:(master) ✗ python3 stochastic.py hey tutu tut tut tut hehehehehe
[['hehehehehe', 119], ['hey', 108], ['tut', 656], ['tutu', 117]]"""
