import fs = require("fs");
const [T, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const testCases = input.map((val) => val.split(" ").map(Number));

const answer = [];
for (const array of testCases) {
  array.sort((x, y) => x - y);
  answer.push(array[array.length - 3]);
}

console.log(answer.join("\n"));
