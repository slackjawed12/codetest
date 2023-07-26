import fs = require("fs");

const [N, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);
const start = input[0];
let result = start;
const counter = input.slice(1);
while (1) {
  const index = counter.findIndex((v) => v === Math.max(...counter));
  if (index < 0 || counter[index] < result) {
    console.log(result - start);
    break;
  }
  counter[index]--;
  result++;
}
