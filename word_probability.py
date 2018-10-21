
from collections import deque
import sys
import string
import re

#w = deque('ghi') adds g, h, i to the the queue
#w.popleft() remove the first item from the queue
#w.pop() standard popping of rightmost item
#w.extend('jkl') adds three items to the stack
#w[0] leftmost (first item)
#w[-1] rightmost (last item)
# queue = last in, last out :: a line at the grocery store
# w.rotate(1) = right rotation (move last to first) and w.rotate(-1) = left rotation (move first to last)

#at some point going to implement deques...



if __name__ == '__main__':
        file = str(sys.argv[1])
        word = sys.argv[2]
        n = sys.argv[3]

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
    punctuation = ["!", "@" , "#" , "$" , "." , ",", "?", ":", ";", "-", "_"]
    for i, word in enumerate(array):
        newWord = ""
        for char in word:
            if char not in punctuation:
                newWord += char
        array[i] = newWord
    return array

def lowercaseArray(array):
    """takes in an array of strings, uses a list comprehension to lowercase each letter"""
    array = [x.lower() for x in array]
    return array

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
        if fileWord == str(word):
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
    for i, key in enumerate(keys):
        if i == 0:
            print("Yo girl if you say \'" + str(word) + "\', there is a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\' next")
        else:
            print("and a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\' next")

def nOrderMarkov(instances):
    myDict = {}
    for i, instance in enumerate(instances):
        myArray = []
        myArray.append(instance[2])
        myArray.append(instance[0])
        myArray+=instance[1]
        print(myArray)
        hashable = ""
        for element in myArray:
            hashable += element
        if hashable not in myDict:
            myDict[hashable] = 1
        else:
            myDict[hashable] += 1
    keys = list(myDict.keys())
    values = list(myDict.values())
    print(keys)
    print(values)
    print(myDict)
    #for i, key in enumerate(keys):
    #    if i == 0:
    #        print("Yo girl if you say \'" + str(word) + "\', there is a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\' next")
    #    else:
    #        print("and a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\' next")


fileWords = lowercaseArray(strip_Punc(arrayFileWords(file)))

fileWordCount = len(arrayFileWords(file))

instances = wordBeforeAfter(fileWords)

#firstOrderMarkov(instances)

nOrderMarkov(instances)


"""
#-------> N-ORDER MARKOV MODEL
myDict = {}
for i, instance in enumerate(instances):
    myArray = []
    myArray.append(str(word))
    myArray+=instance[1]
    #print(myArray)
    hashable = ""
    for element in myArray:
        hashable += element
    if hashable not in myDict:
        myDict[hashable] = 1
    else:
        myDict[hashable] += 1
#------>

#this is returning the word plus n-words before when using N-Order
keys = list(myDict.keys())
values = list(myDict.values())


for i, key in enumerate(keys):
    if i == 0:
        print("Yo girl if you say \'" + str(word) + "\', there is a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\' next")
    else:
        print("and a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\' next")

"""

"""
To do:
-ensure edge cases of input n are handled (index error)
...am I okay with it looping? (taping the beginning to the end)
the end does not tape. 'me' in test.md has no following words and produces an error
#accoutn for edge cases where the word is not in the file, or for when the n causes the program to loop over the file lining up the beginning to the end
#out of index range error when the number was 100000
#find out why n = 103 is the cutoff for 'you.'

-make it an n-order Markov chain.
this is a first order Markov chain, currently.
look at the beforeWords array for each word to get it going.

-consider moving more of the functionality to functions
"""
