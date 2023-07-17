import fs = require("fs");
const [n, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const gcd = function (a: number, b: number): number {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
};

const lcm = function (a: number, b: number): number {
  const G = gcd(a, b);
  return G * (a / G) * (b / G);
};

const answer = input.map((pair) => {
  const [a, b] = pair.split(" ").map(Number);
  return lcm(a, b);
});

console.log(answer.join("\n"));
