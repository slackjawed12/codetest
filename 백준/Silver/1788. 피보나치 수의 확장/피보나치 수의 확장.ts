import fs = require("fs");

const N = parseInt(fs.readFileSync("/dev/stdin").toString().trim());
const MOD = 1000000000;
const dp: number[] = [0, 1];
for (let i = 2; i <= Math.abs(N); i++) {
  dp[i] = (dp[i - 1] + dp[i - 2]) % MOD;
}

const sign = N === 0 ? 0 : N > 0 ? 1 : N % 2 ? 1 : -1;
const answer = [sign, dp[Math.abs(N)]];

console.log(answer.join("\n"));
