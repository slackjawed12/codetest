import fs = require("fs");

const [N, ...matrix] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const horizontal = matrix
  .map((val) => val.split("X"))
  .reduce((acc, cur) => {
    return (acc += cur.filter((val) => val.length >= 2).length);
  }, 0);

const vertical = matrix[0]
  .split("")
  .map((column, i) => {
    const col = matrix.slice(1).reduce((prev, cur) => {
      return prev.concat(cur[i]);
    }, column);
    return col;
  })
  .map((val) => val.split("X"))
  .reduce((acc, cur) => {
    return (acc += cur.filter((val) => val.length >= 2).length);
  }, 0);

console.log(horizontal, vertical);
