let fs = require("fs");
let input = fs.readFileSync('/dev/stdin').toString().split("\n");
input.map((x) => parseInt(x));
let answer = Math.PI * 2 * input[1] + 2 * input[0];

console.log(answer);
