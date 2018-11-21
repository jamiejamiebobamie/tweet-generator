from flask import Flask, render_template
app = Flask(__name__)
from histogram import countWordsDict, countWordsArray, arrayFileWords, strip_Punc, lowercaseArray, keysAsValues
from stochasticFILE import weightedWord
import random
import textgenerator





def chooseFile():
    files = ["Wilde.md", "Shakespeare.md", "Grimm.md", "Carroll.md", "Lovecraft.md", "Woolf.md", "Shelley.md", "Poe.md"]
    return files[random.randint(0,7)]


#file = chooseFile()
#new = lowercaseArray(strip_Punc(arrayFileWords(file)))
#myArr = weightedWord(countWordsDict(new))
#print(myArr, file)



@app.route('/')
def refesh():
    #file = chooseFile()
    ##new = lowercaseArray(strip_Punc(arrayFileWords(file)))
    #new = arrayFileWords(file)
    #count = 0
    #stri = ""
    #while count < 7:
    #    myArr = weightedWord(countWordsDict(new))
    #    stri += myArr
    #    stri += " "
    #    count += 1
    #return "From " + file + ": \'" + stri + "\'"

    def checkChars(myTweet):
        """checks to see how many characters there are in myTweet. if there are less
        than 140 then it returns True."""
        punctuation = [".", "!" , "?"]
        counter = 0
        period = False
        for chars in myTweet:
            counter += 1
            if counter > 140 and chars in punctuation:
                period = True
            elif counter > 300:
                period = True
        if period == False:
            return True
        else:
            return False

    def arrayToString(array):
        """takes in an array and returns the a string of the elements separated by spaces"""
        string = ""
        for elem in array:
            string += str(elem)
        return string

    def nOrderMarkov(instances):
        """takes in an array of tuples (word, [array of n words before word], and next word),
        cycles through the array of tuples and appends the next word and the word to an array,
        and then appends the array of before words

        NEED TO EDIT DOCSTRING..."""
        arrayofArrays = []
        myDict = {}
        for i, instance in enumerate(instances):
            myArray = [] #array in "backwards" chronological order from last word (next) to first word
            myArray.append(instance[2]) #next word
            myArray.append(instance[0]) #word
            myArray+=instance[1] #array of words before word
            arrayofArrays.append(myArray)
        for array in arrayofArrays:
            if tuple(array) not in myDict:
                myDict[tuple(array)] = 1
            else:
                myDict[tuple(array)] += 1
        keys = list(myDict.keys())
        values = list(myDict.values())
        return(keys, values)

    def wordBeforeAfter(array):
        """takes in an array of strings,
        using the global variables word and n,
        looks for instances of the word in the array.
        if an instance of the word is found,
        compiles an array of n words that come before the word.
        returns an array of tuples of
        (1) instance of word,
        (2) array of n words before the instance of the searched word, and
        (3) the next word that comes after the instance of the searched word."""
        instances = []
        for i, fileWord in enumerate(array):
            if fileWord == str.lower(str(word)):
                x = i -1
                beforeWords = []
                #while x > (i - int(n) - 1): #if you want n words before word
                while x > (i - int(n)): #if you want n words after next-word
                    beforeWords.append(array[x])
                    x -= 1
                myTuple = (word, beforeWords, array[i+1])
                instances.append(myTuple)
        return instances

    n = 15
    file = "Grimm.md"
    words = arrayFileWords(file)
    word = arrayFileWords(file)[random.randint(0, len(words)-1)]
    myTweet = str(word)
    upperRange = int(n)                          #creates variety
    lowerRange = (int(n) - (int(n)//1.5))        #consider changing
    if lowerRange < 1:
        lowerRange = 1
    exception = True
    keysValues = nOrderMarkov(wordBeforeAfter(strip_Punc(words)))
    while checkChars(myTweet) and exception:
        try:
            #keysValues = nOrderMarkov(wordBeforeAfter(strip_Punc(words)))
            x = 0
            storeIndex = []
            for i, value in enumerate(keysValues[1]):
                if value > x:
                    x = value
                    storeIndex.append(i)
                    word = keysValues[0][storeIndex[random.randint(((len(storeIndex)-1)//2), (len(storeIndex)-1))]][0]
                    n = random.randint(lowerRange, upperRange)
                    myTweet += " "
                    myTweet += word
                    checkChars(myTweet)
                    value = 0
        except:
            exception = False
    else:
        tweet = myTweet
        print(myTweet)
        print(lowerRange)
        print(upperRange)
        return tweet
        #return (render_template('tweet.html'), tweet)
        #http://127.0.0.1:5000/


#@app.route('/')
#def json():
#    return render_template('tweet.html')


#def webprint():
#    return render_template('tweet.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
