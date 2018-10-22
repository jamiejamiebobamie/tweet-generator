
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
    for i, key in enumerate(keys):
        if i == 0:
            print("Yo girl if you say \'" + str(word) + "\', there is a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\' next")
        else:
            print("and a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\' next")

def nOrderMarkov(instances):
    """takes in an array of tuples (word, [array of n words before word], and next word),
    cycles through the array of tuples and appends the next word and the word to an array,
    and then appends the array of before words
    Does other stuff, see to-do at bottom to see output and how it's right, but also not..."""
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
    for i, key in enumerate(keys):
        if i == 0:
            print("Yo girl if you say \'" + str(word) + "\', there is a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + str(keys[i][0]) + "\' next")
        else:
            print("and a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + str(keys[i][0]) + "\' next")


fileWords = lowercaseArray(strip_Punc(arrayFileWords(file)))

fileWordCount = len(arrayFileWords(file))

instances = wordBeforeAfter(fileWords)

firstOrderMarkov(instances)
nOrderMarkov(instances)


"""
To do:
-ensure edge cases of input n are handled (index error)
...am I okay with it looping? (taping the beginning to the end)
the end does not tape. 'me' in test.md has no following words and produces an error
#accoutn for edge cases where the word is not in the file, or for when the n causes the program to loop over the file lining up the beginning to the end
#out of index range error when the number was 100000
#find out why n = 103 is the cutoff for 'you.'


➜  tweet-generator git:(master) ✗ python3 word_probability.py test.md hungry 3

#first order markov model
Yo girl if you say 'hungry', there is a 28 percent chance that you're going to say 'hungry' next
and a 71 percent chance that you're going to say 'hippos' next

# 3rd order markov model
Yo girl if you say 'hungry', there is a 14 percent chance that you're going to say 'hungry' next
and a 14 percent chance that you're going to say 'hippos' next
and a 14 percent chance that you're going to say 'hippos' next
and a 14 percent chance that you're going to say 'hippos' next
and a 14 percent chance that you're going to say 'hippos' next
and a 14 percent chance that you're going to say 'hungry' next
and a 14 percent chance that you're going to say 'hippos' next




before-words, word ||| next word

past, present ||| future

what are the possible next words you're going to say and what's the probabiltiy of you saying them?

an n-order markov model looks at the words that come before the next word.
the more matches of before-words a next-word has, the more likely you'll say the word next.
the higher the 'n' (or number of words you look at in the past), the less likely the before-words match up,
the lower the probability, but as shown above, what does it matter if the before-words don't match if their next word is the same?

clearly, I have done something wrong...

maybe after, check to see which next words are the same and add up their probabilities?
isn't that just a first order markov model?
"""
