#Sentence scrambler. inp

import random

y = input("\n\nplease enter a sentence to be scrambled. poems that rhyme work the best.\n")

#y = "Jamie is guy who sits and acts real fly if anyone knew what would they do would they sit and watch him too?"

def words(y):
    """looks for the spaces between words, if a character is not a space, it adds it to the string "word"
    if the character is a space it appends the word to the array of words and empties the string-variable "word"
    once all of the characters have been iterated through it returns the array of words"""
    word = ""
    words = []
    for char in y:
        if char != " ":
            word += char
        else:
            words.append(word)
            word = ""
    return words

words = words(y)

def scramble_words(words):
    """takes in an array of strings
    instantiates an empty array
    instantiates an empty string

    cycles through the array of words and takes the word and inserts it in a new array at a random index
    then cycles through the new array and concatenates them to a string
    and returns the string of words

    for some reason this deletes one of the words from the array, but I'm too tired to fix it.
    this was before i knew about the fisher-waits swap.
    """
    new_order = []
    new_message = ""
    counter = 1
    for word in words:
        new_order.insert(random.randint(0, len(words) - counter), word)
        counter += 1
    for item in new_order:
        new_message += (item + " ")
    return new_message


print(scramble_words(words))
