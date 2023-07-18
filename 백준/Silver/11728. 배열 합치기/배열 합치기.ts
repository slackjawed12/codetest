import fs = require("fs");
const [sizes, A, B] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = sizes.split(" ").map(Number);

console.log(
  [...A.split(" ").map(Number), ...B.split(" ").map(Number)]
    .sort((x: number, y: number) => x - y)
    .join(" ")
);
