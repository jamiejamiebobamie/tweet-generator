var fs = require("fs");


function chooseRandomFile(){
    var files = ["Wilde.md", "Shakespeare.md", "Grimm.md", "Carroll.md", "Lovecraft.md", "Woolf.md", "Poe.md"];
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
var fileArray = fileToArray(file);
var word = fileArray[Math.floor(Math.random() * Math.floor(fileArray.length))]
var wBA = wordBeforeAfter(fileArray);
var nexts = nextWords(wBA);
var max = nexts[1]
var vTK = valuestoKeys(nexts);
var keysvTK = Object.keys(vTK)
var v = Math.floor(Math.random() * Math.floor(keysvTK.length));
var tweet = word

while (tweet.length < 140) {
    var wBA = wordBeforeAfter(fileArray);
    var nexts = nextWords(wBA);
    var max = nexts[1]
    var vTK = valuestoKeys(nexts);
    var keysvTK = Object.keys(vTK)
    var v = Math.floor(Math.random() * Math.floor(keysvTK.length));
    word = vTK[keysvTK[v]][Math.floor(Math.random() * Math.floor(vTK[keysvTK[v]].length - 1))]
    tweet = tweet + " " + word
}

var punc = [".", "!", "?", ";"]

if (tweet[(tweet.length) - 1] in punc) {
    tweet = tweet + "-" + file;
} else {
    tweet = tweet + "." + " -" + file;
}
tweet = tweet.charAt(0).toUpperCase() + tweet.slice(1);

console.log(tweet)
