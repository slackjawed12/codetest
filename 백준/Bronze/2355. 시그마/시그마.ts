import fs = require("fs");

const [A, B] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

console.log(((Math.abs(A - B) + 1) * (A + B)) / 2);
