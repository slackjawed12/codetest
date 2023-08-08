import fs = require("fs");

const [D, H, W] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const sqrt = Math.sqrt(H * H + W * W);
console.log(Math.floor((H * D) / sqrt), Math.floor((W * D) / sqrt));
