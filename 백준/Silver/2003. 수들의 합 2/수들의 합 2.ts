import fs = require("fs");

const [first, second] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = first.split(" ").map(Number);
const numbers = second.split(" ").map(Number);

const sums = numbers.reduce(
  (acc, cur) => {
    acc.push(acc[acc.length - 1] + cur);
    return acc;
  },
  [0]
);

let j = 1;
let i = 0;
let answer = 0;
while (j < sums.length) {
  if (sums[j] - sums[i] === M) {
    i++;
    j++;
    answer++;
  } else if (sums[j] - sums[i] < M) {
    j++;
  } else {
    i++;
  }
}

console.log(answer);
