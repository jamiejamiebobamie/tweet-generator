
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
    ##f = open("/usr/share/dict/words", "r")
    fileWords = f.read().split()
    #fileWordCount = len(fileWords)
    f.close()
    return fileWords

fileWords = arrayFileWords(file)
fileWordCount = len(arrayFileWords(file))

def array_Of_Word_And_N_Words_After():
    instances = []
    for i, fileWord in enumerate(fileWords):
        if fileWord == str(word):
            x = i
            instance = []
            while x > (i - int(n)):
                instance.append(fileWords[x])
                x -= 1
            instances.append(instance)
    print(instances)

arrayFileWords(file)
array_Of_Word_And_N_Words_After()

#don't forget edge cases of looking at the first word and the words that come before it (there aren't any...) or looking for n words that exceed the length of the beginning
