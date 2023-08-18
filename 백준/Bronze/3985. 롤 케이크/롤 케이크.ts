import fs = require("fs");

const [L, N, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const numbers = input.map((row) => row.split(" ").map(Number));
const expect = numbers.reduce(
  (acc, cur, index) => {
    const diff = Math.abs(cur[0] - cur[1]);
    if (acc[0] < diff) {
      acc = [diff, index + 1];
    }

    return acc;
  },
  [0, 0]
)[1];

const info = numbers
  .reduce(
    (acc, cur, index) => {
      for (let i = cur[0]; i <= cur[1]; i++) {
        acc[i] = acc[i] === 0 ? index + 1 : acc[i];
      }
      return acc;
    },
    Array.from(Array(parseInt(L) + 1), (_) => 0)
  )
  .reduce(
    (acc, cur) => {
      if (cur !== 0) {
        acc[cur]++;
      }
      return acc;
    },
    Array.from(Array(parseInt(N) + 1), (_) => 0)
  );

const max = info.reduce(
  (acc, cur, index) => {
    if (acc[0] < cur) {
      acc = [Math.max(acc[0], cur), index];
    }

    return acc;
  },
  [0, 0]
);

console.log([expect, max[1]].join("\n"));
