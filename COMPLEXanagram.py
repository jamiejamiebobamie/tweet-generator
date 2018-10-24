from collections import Counter
import random
import sys


f = open("/usr/share/dict/words", "r")

words = f.read().split()
wordCount = len(words)

f.close()

def printWord(testArray):
    word = ""
    for char in testArray:
        word += char
    return word


def anagram(charArray):
    charCount = len(charArray)
    for Dictword in words:
        if len(Dictword) == charCount:
            testArray = []
            for chars in Dictword:
                testArray.append(chars)
            if sorted(testArray) == sorted(charArray) and testArray != charArray and random.choice([True, False]):
                    return(printWord(testArray))
 #how do i not get none if there's an anagram?



if __name__ == '__main__':
    word = sys.argv[1]
    charsArray = []
    for chars in word:
        charsArray.append(chars)
    print(anagram(charsArray))
