import fs = require("fs");

const [numbers, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = numbers.split(" ").map(Number);

const edges = input.map((row) => row.split(" ").map(Number));

const matrix = Array.from(Array(100), (_) => Array.from(Array(100), (_) => 0));

edges.forEach((paper) => {
  const [xi, yi, xf, yf] = paper;

  for (let i = yi - 1; i < yf; i++) {
    for (let j = xi - 1; j < xf; j++) {
      matrix[i][j]++;
    }
  }
});

console.log(
  matrix.reduce((acc, cur) => (acc += cur.filter((val) => val > M).length), 0)
);
