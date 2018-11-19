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


    n = 6
    file = "Grimm.md"
    words = arrayFileWords(file)
    word = arrayFileWords(file)[random.randint(0, len(words)-1)]
    myTweet = str(word)
    upperRange = int(n)                          #creates variety
    lowerRange = (int(n) - (int(n)//1.5))        #consider changing
    if lowerRange < 1:
        lowerRange = 1
    exception = True
    while checkChars(myTweet) and exception:
        try:
            keysValues = nOrderMarkov(wordBeforeAfter(strip_Punc(arrayFileWords(file))))
            #arrayWords = arrayFileWords(file)
            #propers = lookForProper(arrayWords)
            #keysValues = nOrderMarkov(wordBeforeAfter(strip_Punc(lowercase_Array(arrayWords))))
            x = 0
            storeIndex = []
            for i, value in enumerate(keysValues[1]):
                if value > x:                         #right now it is just going to the highest frequency word, use herd_immunity virus_repro-style
                    x = value
                    storeIndex.append(i)
                    word = keysValues[0][storeIndex[random.randint(((len(storeIndex)-1)//2), (len(storeIndex)-1))]][0]       #i could check to see if the word is in the sentence, would completely get rid of repeats tho...
                    n = random.randint(lowerRange, upperRange)#i could check to see if the chars in the word match the up with the last 20 chars, if so use next most frequent word
                    #print(len(storeIndex))
                    #myTweet += str(n)                            #maybe use a queue to do first in, first out of words or chars to consistently check; repetition of the same word is killing me
                    myTweet += " "
                    myTweet += word
                    checkChars(myTweet)
        except:
            exception = False
    else:
        return(arrayToString(uppercaseWords(myTweet)))
        print(lowerRange)
        print(upperRange)


#@app.route('/')
#def json():
#    return render_template('tweet.html')


def webprint():
    return render_template('tweet.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
