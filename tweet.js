var fs = require("fs");


function chooseRandomFile(){
    var files = ["Wilde.md", "Shakespeare.md", "Grimm.md", "Carroll.md", "Lovecraft.md", "Woolf.md", "Shelley.md", "Poe.md"];
    return files[Math.floor(Math.random() * Math.floor(files.length))];
}

function fileToArray(file){
    var text = fs.readFileSync(file).toString('utf-8');
    var words = text.split(" ")
    return words
}

 function arrayToString(array){
     var string = ""
     var i;
     for (i = 0; i < array.length; i++) {
         string += array[i].toString('utf-8') + " "}
     return string;
}

function wordBeforeAfter(array) {
   // """takes in an array of strings,
   // using the global variables word and n,
   // looks for instances of the word in the array.
   // if an instance of the word is found,
   // compiles an array of n words that come before the word.
   // returns an array of tuples of
   // (1) instance of word,
   // (2) array of n words before the instance of the searched word, and
   // (3) the next word that comes after the instance of the searched word."""

   var instances = []
   for (var i = 0; i < array.length; i++) {
       if (array[i] == word){
           var x = i - 1;
           var beforeWords = [];
           while (x > i - n) {
            beforeWords.push(array[x]);
                x -= 1;
                }
                var myInstance = [word, beforeWords, array[i+1]];
                instances.push(myInstance)
                }
             }
             return instances
           }

function nextWords(instances) {
    var lenInt = 0
    var next = {};
    for (var i = 0; i < instances.length; i++) {
        if (instances[i][2] in next) {
            next[instances[i][2]] += 1;
        } else {
            next[instances[i][2]] = 1
        }
        if (lenInt < next[instances[i][2]]){
            lenInt = next[instances[i][2]]
        };
    }
    return ([next, lenInt])
};

function pickRand(nexts){
    var rand = Math.floor(Math.random() * Math.floor(nexts[1]));
    if (rand != 0){
        return rand;
    } else {
        return 1;
    }
}


function valuestoKeys(nexts){
    var max = nexts[1];
    var newDict = {}
    var arrKeys = Object.keys(nexts[0])
    var arrValues = Object.values(nexts[0])
    for (var i = 0; i < arrValues.length; i++){
        if (arrValues[i] in newDict) {
        newDict[arrValues[i]].push(arrKeys[i]);
    } else {
        newDict[arrValues[i]] = [arrKeys[i]]
    }
    }
    return newDict
}


var n = 6;
 var file = chooseRandomFile();
// var file = "test.md"
// var file = "test.md"
var fileArray = fileToArray(file);
// var word = "hippos"
var word = fileArray[Math.floor(Math.random() * Math.floor(fileArray.length))]
var wBA = wordBeforeAfter(fileArray);
var nexts = nextWords(wBA);
var max = nexts[1]
var vTK = valuestoKeys(nexts);

// console.log(nexts);
console.log(file);
// console.log(word);
// console.log(vTK);
var keysvTK = Object.keys(vTK)
// console.log(keysvTK)
var v = Math.floor(Math.random() * Math.floor(keysvTK.length));
// console.log("random index v: " + v)
// var rand_v = (Math.floor(Math.random() * (max - v +1)) + v)
// console.log("random index _v: " + rand_v) //index to pull from
// console.log("value: " + keysvTK[v]) //
// console.log(vTK[keysvTK[v]][0]) // first word
// console.log(vTK[keysvTK[v]][Math.floor(Math.random() * Math.floor(vTK[keysvTK[v]].length - 1))]) // random word
// console.log(Math.floor(Math.random() * Math.floor(vTK[keysvTK[v]].length - 1)))

var tweet = word + " "

while (tweet.length < 140) {
    var wBA = wordBeforeAfter(fileArray);
    var nexts = nextWords(wBA);
    var max = nexts[1]
    var vTK = valuestoKeys(nexts);
    var keysvTK = Object.keys(vTK)
    var v = Math.floor(Math.random() * Math.floor(keysvTK.length));
    word = vTK[keysvTK[v]][Math.floor(Math.random() * Math.floor(vTK[keysvTK[v]].length - 1))]
    tweet = tweet + word + " "
}
tweet = tweet + "-" + file
console.log(tweet)

//Math.floor(Math.random() * (max - min + 1)) + min;


// console.log(Object.keys(vTK)[Math.floor(Math.random() * Math.floor(vTK.length))])

// var rand = pickRand(nexts)

// console.log(rand);
// console.log(max);

//console.log(Math.floor((rand/max) * 100));
// random number between 1 and the max int key value
//divided by the max key value, multiplied by 100 and floored.

//any number equal to or above the number must be put into an array and selected at random.
//words with higher frequencies will always be included in the array.


// Math.floor(Math.random() * Math.floor(fileArr.length)


// console.log(pickRand(nexts));


    // for i, fileWord in enumerate(array):
        // if fileWord == str.lower(str(word)):
            // x = i -1
            // beforeWords = []
            // #while x > (i - int(n) - 1): #if you want n words before word
            // while x > (i - int(n)): #if you want n words after next-word
                // beforeWords.append(array[x])
                // x -= 1
            // myTuple = (word, beforeWords, array[i+1])
            // instances.append(myTuple)
    // return instances
//
// function firstOrderMarkov(arrayOfTuples):
    // """takes in an array of tuples of (word, [array of words before word], next word that comes after word)
    // creates a dictionary of {next word : number of instances}. splits the dictionary into a 'twin index' of two arrays: keys and values.
//
    // "twin index" = keys[0] and values[0] reference the key and value pair of the dictionary that was 'split'.
//
    // for each key the function prints to console what the likelihood is of that key appearing as the next word."""
    // myDict = {}
    // for i, instance in enumerate(arrayOfTuples):
        // if instance[2] not in myDict:
            // myDict[arrayOfTuples[i][2]] = 1
        // else:
            // myDict[arrayOfTuples[i][2]] += 1
    // keys = list(myDict.keys())
    // values = list(myDict.values())
    // print(keys)
    // print(values)
//
// function nOrderMarkov(instances):
    // """takes in an array of tuples (word, [array of n words before word], and next word),
    // cycles through the array of tuples and appends the next word and the word to an array,
    // and then appends the array of before words
//
    // NEED TO EDIT DOCSTRING..."""
    // arrayofArrays = []
    // myDict = {}
    // for i, instance in enumerate(instances):
        // myArray = [] #array in "backwards" chronological order from last word (next) to first word
        // myArray.append(instance[2]) #next word
        // myArray.append(instance[0]) #word
        // myArray+=instance[1] #array of words before word
        // arrayofArrays.append(myArray)
    // for array in arrayofArrays:
        // if tuple(array) not in myDict:
            // myDict[tuple(array)] = 1
        // else:
            // myDict[tuple(array)] += 1
    // keys = list(myDict.keys())
    // values = list(myDict.values())
    // return(keys, values)
//
// function checkChars(myTweet):
    // """checks to see how many characters there are in myTweet. if there are less
    // than 140 then it returns True."""
    // punctuation = [".", "!" , "?"]
    // counter = 0
    // period = False
    // for chars in myTweet:
        // counter += 1
        // if counter > 140 and chars in punctuation:
            // period = True
        // elif counter > 300:
            // period = True
    // if period == False:
        // return True
    // else:
        // return False
    // #and chars in punctuation:
        // #    period = True
    // #if period == True:
    // #    return True
    // #else:
//
// n = 6
// file = "Grimm.md"
// words = arrayFileWords(file)
// word = arrayFileWords(file)[random.randint(0, len(words)-1)]
// myTweet = str(word)
// upperRange = int(n)                          #creates variety
// lowerRange = (int(n) - (int(n)//1.5))        #consider changing
// if lowerRange < 1:
    // lowerRange = 1
// exception = True
// keysValues = nOrderMarkov(wordBeforeAfter(strip_Punc(arrayFileWords(file))))
// while checkChars(myTweet) and exception:
    // try:
//
        // #arrayWords = arrayFileWords(file)
        // #propers = lookForProper(arrayWords)
        // #keysValues = nOrderMarkov(wordBeforeAfter(strip_Punc(lowercase_Array(arrayWords))))
        // x = 0
        // storeIndex = []
        // for i, value in enumerate(keysValues[1]):
            // if value > x:                         #right now it is just going to the highest frequency word, use herd_immunity virus_repro-style
                // x = value
                // storeIndex.append(i)
                // word = keysValues[0][storeIndex[random.randint(((len(storeIndex)-1)//2), (len(storeIndex)-1))]][0]       #i could check to see if the word is in the sentence, would completely get rid of repeats tho...
                // n = random.randint(lowerRange, upperRange)#i could check to see if the chars in the word match the up with the last 20 chars, if so use next most frequent word
                // #print(len(storeIndex))
                // myTweet += str(n)                            #maybe use a queue to do first in, first out of words or chars to consistently check; repetition of the same word is killing me
                // myTweet += " "
                // myTweet += word
                // checkChars(myTweet)
    // except:
        // exception = False
// else:
    // print(arrayToString(uppercaseWords(myTweet)))
    // print(lowerRange)
    // print(upperRange)
