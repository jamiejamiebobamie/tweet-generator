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
var tweet = word

while (tweet.length < 110) {
    var wBA = wordBeforeAfter(fileArray); // file to array of words
    var nexts = nextWords(wBA); // next words
    var max = nexts[1] // max frequency (the frequency of the most likely next word)
    var vTK = valuestoKeys(nexts); // dictionary of frequencies and arrays of words
    var keysvTK = Object.keys(vTK) // array of keys of frequencies
    var v = Math.floor(Math.random() * Math.floor(keysvTK.length)); // random index out of the array of keys of frequencies
    word = vTK[keysvTK[v]][Math.floor(Math.random() * Math.floor(vTK[keysvTK[v]].length - 1))] // random index out of the array of words for frequency 'v'
    tweet = tweet + " " + word // 'word' NOT WEIGHTED -- HOW TO IMPLEMENT??
}

var punc = [".", "!", "?", ";", ",", "\'", "\""]


// attempts at adding a period at the end, but only if there isn't one...

    // if (tweet[(tweet.length) - 1] in punc) { //doesn't work...
        // tweet = tweet + "-" + file;
        // } else {
        // tweet = tweet + "." + " -" + file;
        // };

        // if (tweet.charAt((tweet.length) - 1) in punc) { // doesn't work...
        // tweet = tweet + "-" + file;
        // } else {
        // tweet = tweet + "." + " -" + file;
        // }

//

tweet = tweet + "." + " -" + file;
tweet = tweet.charAt(0).toUpperCase() + tweet.slice(1);

console.log(tweet)
console.log(tweet.length)
