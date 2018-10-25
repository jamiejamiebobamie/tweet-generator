import sys
import random

def arrayToString(array):
    """takes in an array and returns the a string of the elements separated by spaces"""
    string = ""
    for elem in array:
        string += elem + " "
    return string

def rearrange(*args):
    """function takes in arguments from the command line and turns the arguments into an array
    it applies the fisher-waits swap algorithm on the arguments, starting with the first index of the array."""
    count = len(args)
    args = list(args)
    for i in range(count):
        j = random.randint(0, i)
        args[i], args[j] = args[j], args[i]
    return args

if __name__ == '__main__':
    args = sys.argv[1:]
    print(arrayToString(rearrange(*args)))

#SOURCE: https://www.geeksforgeeks.org/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/
