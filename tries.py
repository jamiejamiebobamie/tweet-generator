

#this is an attempt at a 'trie' data structure to store words
# try data structure allows the user to store, find, replace, and delete data in constant time


# class Root():
#
    # def __init__(self):
        # self.tries = []
#
    # def addTrie(self, trie): # trie is a word
        # for i, char in enumerate(trie): #O(n)...
            # new = Tries(char) # for each letter make a new Tries of letter
            # if i == 0: # if first letter
                # self.tries.append(new) # add to root array, stack of pointers to the "first letter" data
            # new.next.append = trie[Tries(i+1)] # set the pointer of each letter to the next letter to know where to go
#
    # def findTrie(self, find): # find is a word, the word your checking for
        # for i, char in enumerate(find): #O(n)...
            # if char in
#
            # else:
                # return False
        # return True


import numpy


def makeAlphabetDict():
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet = {}
    for i, char in enumerate(alpha):
        alphabet[char] = i
    return alphabet

class Tries():
    def __init__(self, current):
        self.current = current #the current node's letter
        self.next = numpy.empty(26, dtype=object) #a fixed array of length 26 for each possible next letters

    def isEmpty(self):
        for nexts in self.next:
            if nexts != None:
                return False
        return True


alphabet = makeAlphabetDict()
print(alphabet)

root = numpy.empty(26, dtype=object) #an array of length 26 filled with None's

def getIndex(char):
    return alphabet[char]

def makeTree(word):
    dict = {} #initialize dictionary
    for i, char in enumerate(word): #go through each of letter of the word
        dict[i] = Tries(char) #make a new trie with the current letter as the Tries.current attribute
        if i == 0: #if it's the first letter of the word
            root[getIndex(char)] = dict[i] #add the trie to the root numpy array
            last = dict[i] # set last to the current Trie (the Trie with the first letter)
        elif i > 0 and last.next[getIndex(char)] == None: #if it's not the first letter and the numpy next array in the 'last' Tries' array is not already filled
            last.next[getIndex(char)] = dict[i] #fill it with the new Trie
            last = dict[i] #set the 'last' attribute to the new Trie
        elif i > 0 and last.next[getIndex(char)] != None:
            last = last.next[getIndex(char)]
            # print('yay')



makeTree("poop")
makeTree("poem")
makeTree("poom")


count = 0
dict = {}

arr = root

for trie in root:
    if trie != None:
        print(trie.current)
        arr = trie.next
        for trie in arr:
            if trie != None:
                print(trie.current)
                arr = trie.next
                for trie in arr:
                    if trie != None:
                        print(trie.current)
                        arr = trie.next
                        for trie in arr:
                            if trie != None:
                                print(trie.current)
                                arr = trie.next

makeTree("tree")
makeTree("poop")
makeTree("pee")
makeTree("phap")
makeTree("tree")
makeTree("poop")
makeTree("pee")
makeTree("poop")
makeTree("tiger")


def get(word):
    print(word)
    next = root
    for i, l in enumerate(word):
        # print(l)
        for trie in next:
            if trie != None and l == trie.current:
                print(trie.current)
                if trie.isEmpty() == False:
                    next = trie.next
                elif trie.isEmpty() == True and i == (len(word)-1):
                    return True
                # print(trie.current, i, trie.next)
    return False



            # print('h')
        # print('k')
    # print('m')
                # if next != None:
                    # next = trie.next
                # else:
                    # return True

# print(get("pee"))

# print(get("poop"))

# print(get("tree"))



# def makeTree(word):
#     # dict = {}
#     for i, char in enumerate(word):
#         char = Tries(char)
#         if i == 0:
#             root.append(char)
#         else:
#             last.next.append(char)
#         last = char
#         # print(last, last.current, last.next)
#     for las in last.next:
#         # print(last, last.current, last.next, las, las.current, las.next)
#         print(last.next, las.next)

# def inTree(word):
    # print(word)
    # for i, char in enumerate(word):
        # if i == 0:
            # for tries in root:
                # if tries.current == char:
                    # last = tries
                    # print(last.current)
                # else:
                    # return False
        # else:
            # for tries in last.next:
                    # if tries.current == char:
                        # print((char, tries.current, tries.current == char))
                        # last = tries
                        # print(last.current)
                    # else:
                        # return False
    # else:
        # return True





# def inTree(word):
#     print(word)
#     last = root
#     print(len(last))
#     # print(type(last))
#     for i, char in enumerate(word):
#         # while i < (len(word)-1):
#         for tries in last:
#             if tries.current == char:
#                 print((i, (len(word)-1), tries.current == char, tries.current, char))
#                 last = tries.next
#                 continue
#                 print((tries.current == char, char))
#             # else:
#                 # return False
#                 print((i, (len(word)-1), tries.current == char, tries.current, char))
#     # return True



# print(len(root))
#
# for roots in root:
    # print(roots)
    # print(root)

# makeTrie("hello")

# print(inTree("poop"))


# print(inTree("hello"))

# makeTrie("hen")
# print(inTree("hen"))
# print(inTree("pee"))

# last = root
# print(len(root))
# for trie in last:
    # print(trie.current)
    # last = trie.next
    # print(len(last))
    # for trie in last:
        # print(trie.current)




# from : https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1

# from typing import Tuple
#
#
# class TrieNode(object):
#     """
#     Our trie node implementation. Very basic. but does the job
#     """
#
#     def __init__(self, char: str):
#         self.char = char
#         self.children = []
#         # Is it the last character of the word.`
#         self.word_finished = False
#         # How many times this character appeared in the addition process
#         self.counter = 1
#
#
# def add(root, word: str):
#     """
#     Adding a word in the trie structure
#     """
#     node = root
#     for char in word:
#         found_in_child = False
#         # Search for the character in the children of the present `node`
#         for child in node.children:
#             if child.char == char:
#                 # We found it, increase the counter by 1 to keep track that another
#                 # word has it as well
#                 child.counter += 1
#                 # And point the node to the child that contains this char
#                 node = child
#                 found_in_child = True
#                 break
#         # We did not find it so add a new chlid
#         if not found_in_child:
#             new_node = TrieNode(char)
#             node.children.append(new_node)
#             # And then point node to the new child
#             node = new_node
#     # Everything finished. Mark it as the end of a word.
#     node.word_finished = True
#
#
# def find_prefix(root, prefix: str) -> Tuple[bool, int]:
#     """
#     Check and return
#       1. If the prefix exsists in any of the words we added so far
#       2. If yes then how may words actually have the prefix
#     """
#     node = root
#     # If the root node has no children, then return False.
#     # Because it means we are trying to search in an empty trie
#     if not root.children:
#         return False, 0
#     for char in prefix:
#         char_not_found = True
#         # Search through all the children of the present `node`
#         for child in node.children:
#             if child.char == char:
#                 # We found the char existing in the child.
#                 char_not_found = False
#                 # Assign node as the child containing the char and break
#                 node = child
#                 break
#         # Return False anyway when we did not find a char.
#         if char_not_found:
#             return False, 0
#     # Well, we are here means we have found the prefix. Return true to indicate that
#     # And also the counter of the last node. This indicates how many words have this
#     # prefix
#     return True, node.counter
#
# if __name__ == "__main__":
#     root = TrieNode('*')
#     add(root, "hackathon")
#     add(root, 'hack')
#
#     print(find_prefix(root, 'hac'))
#     print(find_prefix(root, 'hack'))
#     print(find_prefix(root, 'hackathon'))
#     print(find_prefix(root, 'ha'))
#     print(find_prefix(root, 'hammer'))
