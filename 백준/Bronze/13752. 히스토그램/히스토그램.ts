import fs = require("fs");
const [n, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

console.log(input.map((val) => "=".repeat(parseInt(val))).join("\n"));
