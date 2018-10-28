"""takes in a text file, counts the frequency of words in the text
returns a dictionary of word:frequency, key:value pairs"""

import sys


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
    punctuation = ["@" , "#" , "$" , ":", ";", "_", "*" , "}" , "[" , "{" , "]" , "," , ".", "!" , "?"] #took out single and double quotes from this array
    for i, word in enumerate(array):
        newWord = ""
        for char in word:
            if char not in punctuation:
                newWord += char
        array[i] = newWord
    return array

def lowercaseArray(array):
    """takes in an array of strings, uses a list comprehension to lowercase each letter"""
    #uppercase = ["I", "\'I" , "\"I"]
    array = [x.lower() for x in array] # if x not in uppercase]
    return array




#DICTIONARY HISTOGRAM ---------
#def countWords(array):
#    """takes in an array of words (strings) and sorts them into a dictionary
#    with the frequency (the # of times) that the word appears in the text as it's value,
#    and the word as the key."""
#    myDict = {}
#    for word in array:
#        if word not in myDict:
#            myDict[word] = 1
#        else:
#            myDict[word] += 1
#    return myDict
#
#def unique_words(histogram):
#    """takes in a histogram and returns the number of unique keys in it"""
#    return len(histogram.keys())
#
#def frequency(histogram, word):
#    """takes in a histogram and a word and returns the value of the word if the
#    key exists in the dictionary, otherwise returns 0 """
#    word = word.lower()
#    if word in histogram:
#        return histogram[word]
#    else:
#        return str(0)
##^^^^^DICTIONARY HISTOGRAM^^^^^




#List of lists HISTOGRAM ---------
#def countWords(array):
#    """takes in an array of words (strings) and sorts them alphabetically
#    cycles through the array and counts the entries in order,
#   appending an array of the word and the word's frequency to array 'A'."""
#    array.sort()
#    A = []
#    count = 0
#    index = None
#    for word in array:
#        if word == index:
#            count += 1
#        else:
#            A.append([index, count])
#            index = word
#            count = 1
#    else:
#        A.append([index, count])
#        A.pop(0)
#    return A
#
#def unique_words(histogram):
#    """takes in a histogram and returns the number of unique items in the array"""
#    return len(histogram)
#
#def frequency(histogram, word):
#    """takes in a histogram and a word and returns the # of times the word appears,
#    according to second entry in the entry's array"""
#    word = word.lower()
#    for entry in histogram:
#        if entry[0] == word:
#            return entry[1]
#    else:
#        return "Your word is not in the text."
#^^^^^list of lists HISTOGRAM^^^^^

#List of tuples HISTOGRAM ---------
def countWords(array):
    """takes in an array of words (strings) and sorts them into a dictionary
    with the frequency (the # of times) that the word appears in the text as it's value,
    and the word as the key."""
    array.sort()
    A = []
    count = 0
    index = None
    for word in array:
        if word == index:
            count += 1
        else:
            A.append([index, count])
            index = word
            count = 1
    else:
        A.append([index, count])
        A.pop(0)
    return A

def unique_words(histogram):
    """takes in a histogram and returns the number of unique keys in it"""
    return len(histogram)

def frequency(histogram, word):
    """takes in a histogram and a word and returns the value of the word if the
    key exists in the dictionary, otherwise returns 0 """
    word = word.lower()
    for entry in histogram:
        if entry[0] == word:
            return entry[1]
    else:
        return "Your word is not in the text."
#^^^^^list of tuples HISTOGRAM^^^^^


if __name__ == '__main__':
    file = str(sys.argv[1])
    print(frequency(countWords(lowercaseArray(strip_Punc(arrayFileWords(file)))), "Jump"))
