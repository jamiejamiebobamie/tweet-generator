from collections import Counter
import random
import sys
import time
start = time.time()

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


def select(number):
    """x is a counter for the while loop
    wordsFunc is an empty array
    words_spaced is an empty string

    number is input by the user when calling the function from the command line

    while x is less than the requested number of words
    append a random word from the dictionary.
    increment the counter by one.
    repeats are possible, but unlikely given the number of words in the array words.

    once the correct number of words have been reached,
    cycle through the elements of the array of words and stringify each word
    and then add a space.
    there is a single empty space after the last element.
    return the string of spaced words.
    """
    words_spaced = ""
    wordsFunc = []
    x = 0

    while x < number:
        wordsFunc.append(words[random.randint(0, (len(words) - 1))])
        x += 1

    for word in wordsFunc:
        words_spaced += str(word)
        words_spaced += " "

    return words_spaced

if __name__ == '__main__':
    #start = time.time()
    number = sys.argv[1]
    number = int(number)
    words = dict()
    #end = time.time()
    print(select(number))
    #print(end-start)
