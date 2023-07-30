import fs = require("fs");

const input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());

const countOfNumbers: number[] = [];

let cur = input;
let digit = 9;
while (cur > 0) {
  const count = Math.min(digit, cur);
  digit *= 10;
  cur -= count;
  countOfNumbers.push(count);
}

const answer = countOfNumbers
  .map((count, i) => (i + 1) * count)
  .reduce((acc, cur) => (acc += cur));

console.log(answer);
