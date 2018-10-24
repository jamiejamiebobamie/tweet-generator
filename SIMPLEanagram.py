import sys
import random


def anagram(*args):
    count = len(args)
    args = list(args)
    args = [x.lower() for x in args]
    words = []
    for x in args:
        word = []
        for chars in x:
            word.append(chars)
        words.append(word)
    #implement the swapping behavior used in rearrage.py
    #on each array in the array and then convert the array to a string
    #using a nested for loop


if __name__ == '__main__':
    args = sys.argv[1:]
    print(anagram(*args))
