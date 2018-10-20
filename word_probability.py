
from collections import deque
import sys


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


def array_of_N_Words_After():
    instances = []
    for i, fileWord in enumerate(fileWords):
        if fileWord == str(word):
            x = i -1
            afterWords = []
            while x > (i - int(n) - 1):
                afterWords.append(fileWords[x])
                x -= 1
            myTuple = (word, afterWords, fileWords[i+1])
            instances.append(myTuple)
    return instances

fileWords = arrayFileWords(file)
fileWordCount = len(arrayFileWords(file))
instances = array_of_N_Words_After()

myDict = {}
for i, instance in enumerate(instances):
    if instance[2] not in myDict:
        myDict[instances[i][2]] = 1
    else:
        myDict[instances[i][2]] += 1

keys = list(myDict.keys())
values = list(myDict.values())


for i, key in enumerate(keys):
    if i == 0:
        print("Yo girl if you say \'" + str(word) + "\', there is a " + str(int(values[i] / sum(values)*100)) + " percent chance that you're going to say \'" + keys[i] + "\'")
    else:
        print("and a " + str(values[i] / sum(values)) + " percent chance that you're going to say \'" + keys[i] + "\'.")

#To do:

"""
-sanitzie the input :: stringify it, strip it of punctuation and make everything lowercase

-ensure edge cases of input n are handled (index error)

-look at the above for-loop and determine why myDict[instances[i][2]] isn't registering different outputs for input "hungry"
"""

#accoutn for edge cases where the word is not in the file, or for when the n causes the program to loop over the file lining up the beginning to the end

#notice:: punctuation is being counted as letters causing you and you. to be differently (and in the case of test.md, you to not be counted at all)

#out of index range error when the number was 100000
#find out why n = 103 is the cutoff for 'you.'

#strip the fileWordsArray of uppercase words and punctuation

# "hungry" has two instances ... this isn't working... "hungry, hungry" and "hungry hippos"...
#Yo girl if you say 'hungry', there is a 80 percent chance that you're going to say 'hippos' and a 0.2 percent chance that you're going to say 'hippos,'.
#the input "hungry" should result in "hungry" and "hippos"...
