import sys
import string

def arrayFileWords(file):
    """opens a file, puts the words into an array,
    closes the file and returns the array of strings"""
    f = open(file, "r")
    array = f.read().split()
    f.close()
    return array

def arrayToString(array):
    """takes in an array and returns the a string of the elements separated by spaces"""
    string = ""
    for elem in array:
        string += str(elem)
    return string

def uppercaseWords(string):
    punctuation = ["." , "!" , "?"]
    array = []
    for char in string:
        array.append(char)
    for i, element in enumerate(array):
        #print(array[i-2])
        if array[i-2] in punctuation and i > 2:
            print((True, str(element)))
            array[i] = element.upper()
    return array

"""def lookForProper(string):
    count = 1
    array = string.split()
    proper = []
    noproper = []
    for word in array:
        for i, char in enumerate(word):
            if i == 0 and char.islower() and word.title() in proper:
                proper.remove(word.title())
                noproper.append(word)
                print(True)
            if char.istitle() and word not in proper and word not in noproper:
                proper.append(word)
    return (proper, array)"""

def lookForProper(array):
    propers = []
    noproper = []
    for word in array:
        for i, char in enumerate(word):
            if i == 0 and char.islower() and word.title() in propers:
                propers.remove(word.title())
                noproper.append(word)
            if char.istitle() and word not in propers and word not in noproper:
                propers.append(word)
    return propers

def lowercaseArray(array):
    """takes in an array of strings, uses a list comprehension to lowercase each letter"""
    uppercase = ["I", "\'I" , "\"I"]
    array = [x.lower() for x in array if x not in uppercase and x not in propers]
    return array


def lowercase_Array(array):
    newArray = []
    uppercase = ["I", "\'I" , "\"I"]
    for word in array:
        if word in uppercase or word in propers:
            newArray.append(word)
        else:
            newArray.append(word.lower())
    return newArray

if __name__ == '__main__':
        file = str(sys.argv[1])
        #print(arrayFileWords(
        propers = lookForProper(arrayFileWords(file))
        print(lowercase_Array(arrayFileWords(file)))
