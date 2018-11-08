from flask import Flask
app = Flask(__name__)
from histogram import countWordsDict, countWordsArray, arrayFileWords, strip_Punc, lowercaseArray, keysAsValues
from stochasticFILE import weightedWord
import random

def chooseFile():
    files = ["Wilde.md", "Shakespeare.md", "Grimm.md", "Carroll.md", "Lovecraft.md"]
    return files[random.randint(0,3)]


#file = chooseFile()
#new = lowercaseArray(strip_Punc(arrayFileWords(file)))
#myArr = weightedWord(countWordsDict(new))
#print(myArr, file)



@app.route('/')
def refesh():
    file = chooseFile()
    #new = lowercaseArray(strip_Punc(arrayFileWords(file)))
    new = arrayFileWords(file)
    count = 0
    stri = ""
    while count < 7:
        myArr = weightedWord(countWordsDict(new))
        stri += myArr
        stri += " "
        count += 1
    return "From " + file + ": \'" + stri + "\'"
