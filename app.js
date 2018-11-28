const express = require('express')
const app = express()
// const tweet = require('./tweet.js');

var exphbs = require('express-handlebars');

app.engine('handlebars', exphbs({ defaultLayout: 'main' }));
app.set('view engine', 'handlebars');

app.use(express.static('views/finals'));
app.use(express.static('views/public'));

var mongoose = require('mongoose');
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost/rotten-potatoes');


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

function wordBeforeAfter(array, word, n) {
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

var punc = [".", "!", "?", ";", ","]

var myAuthors = {
    "Poe": "Edgar Allan Poe",
    "Lovecraft": "HP Lovecraft",
    "Woolf": "Virginia Woolf",
    "Shakespeare": "William Shakespeare",
    "Carroll": "Lewis Carroll",
    "Wilde": "Oscar Wilde",
    "Grimm": "The Brothers Grimm",
}

function check(tweet){ //slows it down like crazy and all of the if statements don't work properly...
    var even = false;
    var count = 0;

    for (var i=0; i < (tweet.length); i++) {

        if (i == 0 && tweet[i] == " ") {
            tweet = tweet.substring(1, tweet.length);
        }

        if (tweet[i] == "\"") {
            count++;
        }
        if (tweet.substring(tweet.length-3, tweet.length-1) == "and") {
            tweet = tweet + "...";
        }
        if (i == (tweet.length-1) && tweet[i] == ",") {
                tweet = tweet.substring(0, tweet.length-1);
                console.log(tweet[i])
        // } else if (i == (tweet.length-1) && punc.includes(tweet[i]) ){
            //
        // } else if (i == (tweet.length-1) && punc.includes(tweet[i]) ){
            // tweet = tweet.charAt(0).toUpperCase() + tweet.slice(1);
            // tweet = tweet + "."
        } else if (i == (tweet.length-1) && punc.includes(tweet[i])) {
            tweet = tweet;
        } else {
            tweet = tweet.charAt(0).toUpperCase() + tweet.slice(1);
            tweet = tweet + ".";
        }

    if (count%2 != 0 && count != 0) {
        even = true;
    } else {
        even = false;
    }
    return [tweet, even]
}}

function run(){
var n = 6;
var file = chooseRandomFile();
var fileArray = fileToArray(file);
var word = fileArray[Math.floor(Math.random() * Math.floor(fileArray.length))]
var tweet = word

while (tweet.length < 110) {
    var wBA = wordBeforeAfter(fileArray, word, n); // file to array of words
    var nexts = nextWords(wBA); // next words
    var max = nexts[1] // max frequency (the frequency of the most likely next word)
    var vTK = valuestoKeys(nexts); // dictionary of frequencies and arrays of words
    var keysvTK = Object.keys(vTK) // array of keys of frequencies
    var v = Math.floor(Math.random() * Math.floor(keysvTK.length)); // random index out of the array of keys of frequencies
    word = vTK[keysvTK[v]][Math.floor(Math.random() * Math.floor(vTK[keysvTK[v]].length - 1))] // random index out of the array of words for frequency 'v'
    tweet = tweet + " " + word // 'word' NOT WEIGHTED -- HOW TO IMPLEMENT??
}




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

var author = file.slice(0, -3)

var thing = check(tweet)
var odd = thing[1]
tweet = thing[0]

if (odd){
    tweet = tweet + "\"" + " -" + myAuthors[author];
} else {
    tweet = tweet + " -" + myAuthors[author];
}

 tweet = tweet.charAt(0).toUpperCase() + tweet.slice(1);

return tweet.toString()}

// var titleElement = document.getElementById('title');
// var tweet = run()




// app.listen(8000, () => {
  // console.log('App listening on port 7000!')
// })

const port = process.env.PORT || 8000;
// var server = app.listen(process.env.PORT || 8000, function () {
  // var port = server.address().port;
  // console.log("Express is working on port " + port);
// });

app.get('/', (req, res) => {
  res.render('tweet', { msg: run() });
})
app.listen(port);
