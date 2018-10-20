from collections import Counter
import random
import sys


f = open("/usr/share/dict/words", "r")

words = f.read().split()
wordCount = len(words)

f.close()


def select(number):
    words_spaced = ""
    wordsFunc = []
    x = 0

    while x < number:
        wordsFunc.append(words[random.randint(0, (wordCount - 1))])
        x += 1

    for word in wordsFunc:
        words_spaced += str(word)
        words_spaced += " "

    return words_spaced

if __name__ == '__main__':
    number = sys.argv[1]
    number = int(number)
    print(select(number))
