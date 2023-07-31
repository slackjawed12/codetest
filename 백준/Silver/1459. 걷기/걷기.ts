import fs = require("fs");

const [X, Y, W, S] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

if (2 * W < S) {
  console.log(W * (X + Y));
} else if (W < S) {
  console.log(S * Math.min(X, Y) + W * (Math.max(X, Y) - Math.min(X, Y)));
} else {
  console.log((X + Y) % 2 ? S * (Math.max(X, Y) - 1) + W : S * Math.max(X, Y));
}
