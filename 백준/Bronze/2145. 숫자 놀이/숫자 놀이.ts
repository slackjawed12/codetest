import fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .slice(0, -1)
  .map(Number);

console.log(
  input
    .map((val) => {
      while (Math.floor(val / 10) !== 0) {
        val = val
          .toString()
          .split("")
          .reduce((acc, cur) => (acc += parseInt(cur)), 0);
      }
      return val;
    })
    .join("\n")
);
