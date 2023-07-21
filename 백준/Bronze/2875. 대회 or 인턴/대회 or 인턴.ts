import fs = require("fs");

const [N, M, K] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const first = Math.min(Math.floor(N / 2), M);
const [rw, rm] = [N - 2 * first, M - first];
const res = Math.max(0, K - rw - rm);

const answer = first - Math.ceil(res / 3);
console.log(answer);
