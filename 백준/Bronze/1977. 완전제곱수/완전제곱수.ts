import fs = require("fs");

const [M, N] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const arr: number[] = [];
for (let i = 1; i * i <= N; i++) {
  if (i * i >= M && i * i <= N) {
    arr.push(i * i);
  }
}

console.log(
  arr.length === 0
    ? -1
    : [arr.reduce((acc, cur) => (acc += cur), 0), arr[0]].join("\n")
);
