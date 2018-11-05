#https://www.hackerrank.com/challenges/the-minion-game/forum

#s = raw_input()

#vowels = 'AEIOU'
#
#kevsc = 0
#stusc = 0
#for i in range(len(s)):
#    if s[i] in vowels:
#        kevsc += (len(s)-i)
#    else:
#        stusc += (len(s)-i)
#
#if kevsc > stusc:
#    print "Kevin", kevsc
#elif kevsc < stusc:
#    print "Stuart", stusc
#else:
#    print "Draw"

#   -from abitrolly on hackerrank.com, apprently we don't need to check if the substring is in fact a word...


#my solution below:

from dictionary_words import dict, select
import random
import sys

if __name__ == '__main__':
    #start = time.time()
    word = sys.argv[1]
    words = dict()

words = dict()

#word = words[random.randint(0, len(words)-1)]

vowels = ["a", "e", "i", "o", "u"]

cons = ["b" , "c" , "d" , "f" , "g" , "h" , "j" , "k" , "l" , "m" , "n" , "p" , "q" , "r" , "s" , "t" , "v" , "w" , "x" , "z"]

vowelScore = 0 #Kevin
conScore = 0 #Stuart

for i, char in enumerate(word):
    if char in vowels:
        x = i
        new = ""
        while x < len(word):
            new += word[x]
            if new in words:
                vowelScore += len(new)
                x += 1
        #        print(new, vowelScore)
            else:
                x += 1
    elif char in cons:
        x = i
        new = ""
        while x < len(word):
            new += word[x]
            if new in words:
                conScore += len(new)
                x += 1
        #        print(new, conScore)
            else:
                x += 1
if vowelScore > conScore:
    print("Kevin " + str(vowelScore))
elif vowelScore < conScore:
    print("Stuart " + str(vowelScore))
else:
    print("Draw!")
#print(word, len(word), vowelScore, conScore)
