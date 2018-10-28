from collections import Counter
import random
import sys

def dict():
    """opens the dictionary-words file at the path and assigns the file to f
    reads f and splits each word into an array element of the words array
    closes the file f
    and returns the array of dictionary words
    """
    f = open("/usr/share/dict/words", "r")
    words = f.read().split()
    f.close()
    return words

def printWord(testArray):
    """takes in an array and returns a string of the elements separated by spaces"""
    word = ""
    for char in testArray:
        word += char
    return word


def anagram(charArray):
    """takes in an array of character from a single word
    gets the length of the array / the number of characters"""
    anagrams = []
    charCount = len(charArray)
    for Dictword in words:
        if len(Dictword) == charCount:
            testArray = []
            for chars in Dictword:
                testArray.append(chars)
            if sorted(testArray) == sorted(charArray) and testArray != charArray:
                anagrams.append(testArray)
    else:
        if len(anagrams)>0:
            return(printWord(random.choice(anagrams)))
        else:
            return "No anagram..."



if __name__ == '__main__':
    word = sys.argv[1]
    charsArray = []
    for chars in word:
        charsArray.append(chars)
    words = dict()
    print(anagram(charsArray))
