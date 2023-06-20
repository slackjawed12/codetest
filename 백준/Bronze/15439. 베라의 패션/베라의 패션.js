let fs = require("fs");
let input = parseInt(fs.readFileSync('/dev/stdin').toString());
// let input = parseInt(fs.readFileSync("test.txt").toString());

let answer = input * (input - 1);

console.log(answer);
