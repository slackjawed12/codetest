import fs = require("fs");

const [N, ...numbers] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const dp = numbers.reduce(
  (prev, cur) => {
    prev.push(Math.max(prev[prev.length - 1] * cur, cur));
    return prev;
  },
  [0]
);

console.log(
  dp.reduce((prev, cur) => Math.max(prev, cur), -Infinity).toFixed(3)
);
