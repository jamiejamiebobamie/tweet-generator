"""➜  tweet-generator git:(master) python3 SIMPLEanagram.py in place anagrams that do not spell a word
  in eclpa gaamsarn taht do not pells a rdow"""
import sys
import random



def arrayToString(array):
    """takes in an array and returns the a string of the elements separated by spaces"""
    string = " "
    for elem in array:
        string += str(elem)
    return string

def rearrange(args):
    """review how to import functions from your own python files.
    this should be imported at the top instead of redefined here.
    ***
    function takes in arguments from the command line and turns the arguments into an array
    it applies the fisher-waits swap algorithm on the arguments, starting with the first index of the array."""
    count = len(args)
    for i in range(count):
        j = random.randint(0, i)
        args[i], args[j] = args[j], args[i]
    return args

def anagram(*args):
    """takes in arguments (a tuple).
    gets the count. turns the tuple into an array in order to be change it.
    applies a list comprehension to the array, lowering each letter.
    creates an array of characters for each word in the array,
    replaces the string of words with an array of the word's characters
    applies the rearrange method to each array of characters
    and then turns the array back into a string
    replaces the corect array element with a stringified, rearranged word.
    returns the array of reaaranged strings"""
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
    """if name = main, take in arguments and apply the anagram method to it and then stringify it."""
    args = sys.argv[1:]
    print(arrayToString(anagram(*args)))
