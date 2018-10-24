import sys
import random

def arrayToString(array):
    string = " "
    for elem in array:
        string += str(elem)
    return string

def rearrange(args):
    count = len(args)
    for i in range(count):
        j = random.randint(0, i)
        args[i], args[j] = args[j], args[i]
    return args

def anagram(*args):
    count = len(args)
    args = list(args)
    args = [x.lower() for x in args]
    words = []
    for i, x in enumerate(args):
        word = []
        for chars in x:
            word.append(chars)
        args[i] = arrayToString(rearrange(word))
    return args

if __name__ == '__main__':
    args = sys.argv[1:]
    print(arrayToString(anagram(*args)))
