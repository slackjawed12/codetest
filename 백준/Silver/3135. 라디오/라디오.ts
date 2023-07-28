import fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [A, B] = input[0].split(" ").map(Number);
const [N, ...f] = input.slice(1).map(Number);
const firstButton = Math.abs(A - B);
const minButton = f.reduce((prev, cur) => {
  return (prev = Math.min(prev, Math.abs(cur - B) + 1));
}, Infinity);

console.log(Math.min(firstButton, minButton));
