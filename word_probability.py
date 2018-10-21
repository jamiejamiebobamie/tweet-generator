
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




if __name__ == '__main__':
        file = str(sys.argv[1])
        word = sys.argv[2]
        n = sys.argv[3]

def arrayFileWords(file):
    f = open(file, "r")
    #f = open("/usr/share/dict/words", "r")
    fileWords = f.read().split()
    #fileWordCount = len(fileWords)
    f.close()
    return fileWords

#def array_of_N_Words_After():
#    #the text wraps. the index of 0 - 1 = the last index of the file
#    instances = []
#    for i, fileWord in enumerate(fileWords):
#        if fileWord == str(word):
#            x = i -1
#            instance = []
#            while x > (i - int(n) - 1):
#                instance.append(fileWords[x])
#                x -= 1
#            instances.append(instance)
#    print(instances)

def strip_Punc():
    punctuation = ["!", "@" , "#" , "$" , "." , ","]
    for i, word in enumerate(fileWords):
        newWord = ""
        for char in word:
            if char not in punctuation:
                newWord += char
        fileWords[i] = newWord


fileWords = arrayFileWords(file)
fileWords = [x.lower() for x in fileWords] #a lit comprehension that lowercases everything ... reconsider where this is in the code structure
fileWordCount = len(arrayFileWords(file))
strip_Punc()

def array_of_N_Words_After():
    instances = []
    for i, fileWord in enumerate(fileWords):
        if fileWord == str(word):
            x = i -1
            beforeWords = []
            while x > (i - int(n) - 1):
                beforeWords.append(fileWords[x])
                x -= 1
            myTuple = (word, beforeWords, fileWords[i+1])
            instances.append(myTuple)
    return instances

instances = array_of_N_Words_After()

#myDict_beforeWords = {}
#myArray_afterWords = []
myDict = {}
for i, instance in enumerate(instances):
    if instance[2] not in myDict:
        myDict[instances[i][2]] = 1
    else:
        myDict[instances[i][2]] += 1
#   if instance[2] not in myArray_afterWords and instance[1] not in myDict_beforeWords:                    ...this is the right idea?

#        myDict_beforeWords[instances[i][2]] = 1
#        myArray_afterwords.append(instances[i][1])
#    else:
#        myDict_beforeWords[instances[i][2]] += 1

keys = list(myDict.keys())
values = list(myDict.values())


for i, key in enumerate(keys):
    if i == 0:
        print("Yo girl if you say \'" + str(word) + "\', there is a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\'")
    else:
        print("and a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\'.")

#To do:

"""
-sanitzie the input :: stringify it, strip it of punctuation and make everything lowercase

-ensure edge cases of input n are handled (index error)
...am I okay with it looping? (taping the beginning to the end)

-look at the above for-loop and determine why myDict[instances[i][2]] isn't registering different outputs for input "hungry" (repeated words)
...it's skipping the first repeated "hungry"'s (2 of them) because they're uppercase...
"""

#accoutn for edge cases where the word is not in the file, or for when the n causes the program to loop over the file lining up the beginning to the end

#notice:: punctuation is being counted as letters causing you and you. to be differently (and in the case of test.md, you to not be counted at all)

#out of index range error when the number was 100000
#find out why n = 103 is the cutoff for 'you.'

#strip the fileWordsArray of uppercase words and punctuation

# "hungry" has two instances ... this isn't working... "hungry, hungry" and "hungry hippos"...
#Yo girl if you say 'hungry', there is a 80 percent chance that you're going to say 'hippos' and a 0.2 percent chance that you're going to say 'hippos,'.
#the input "hungry" should result in "hungry" and "hippos"...
