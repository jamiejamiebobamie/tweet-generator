#hackerrank 'Word Order' problem
#username "Boki" 's solution below mine in comments 

import sys

if __name__ == '__main__':
    num = int(sys.argv[1])

n = 0
words = []
while n < num:
    word = input()
    words.append(word)
    n += 1

dict = {}
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
print(len(dict))

s = ""
for word in words:
    s += str(dict[word])
    s += " "
print(s)



#Boki 2 years ago
#a really elegant solution
#
#from collections import Counter, OrderedDict
#class OrderedCounter(Counter, OrderedDict):
#    pass
#d = OrderedCounter(input() for _ in range(int(input())))
#print(len(d))
#print(*d.values())

#-https://www.hackerrank.com/challenges/word-order/forum
