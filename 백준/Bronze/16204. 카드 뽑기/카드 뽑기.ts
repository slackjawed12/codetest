import fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .split(" ")
  .map((v) => parseInt(v));

console.log(
  Math.min(input[1], input[2]) +
    Math.min(input[0] - input[1], input[0] - input[2])
);
export {};
