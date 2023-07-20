import fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, M] = input[0].split(" ").map(Number);
const mat = input.slice(1, N + 1).map((row) => {
  return row.split(" ").map(Number);
});
const [K, ...targets] = input.slice(N + 1);

const answer = targets.map((row) => {
  const [yi, xi, yf, xf] = row.split(" ").map((v) => parseInt(v) - 1);
  let sum = 0;
  for (let i = yi; i <= yf; i++) {
    for (let j = xi; j <= xf; j++) {
      sum += mat[i][j];
    }
  }

  return sum;
});

console.log(answer.join("\n"));
