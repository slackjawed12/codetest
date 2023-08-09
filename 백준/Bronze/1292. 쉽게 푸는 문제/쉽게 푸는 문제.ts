import fs = require("fs");

const [A, B] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let count = 1;
let num = 1;
const S = Array.from(Array(B + 1), (_) => {
  if (count === num) {
    count = 1;
    return num++;
  }
  count++;
  return num;
}).reduce(
  (acc: number[], cur, i) => {
    acc.push(cur + acc[acc.length - 1]);
    return acc;
  },
  [0]
);

console.log(S[B] - S[A - 1]);
