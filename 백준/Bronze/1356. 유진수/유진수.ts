import fs = require("fs");

const N = fs.readFileSync("/dev/stdin").toString().trim();

const multiply = (s: string) => {
  return s
    .split("")
    .map(Number)
    .reduce((acc, cur) => (acc *= cur), 1);
};

const isValid = (n: string) => {
  for (let i = 0; i < N.length - 1; i++) {
    const x = N.slice();
    const headResult = multiply(x.slice(0, i + 1));
    const tailResult = multiply(x.slice(i + 1));
    if (headResult === tailResult) {
      return true;
    }
  }

  return false;
};

const result = isValid(N);

console.log(result ? "YES" : "NO");
