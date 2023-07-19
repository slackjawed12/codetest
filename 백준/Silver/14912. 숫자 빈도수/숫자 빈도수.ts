import fs = require("fs");
const [n, d] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const digitCounter: Map<number, number> = new Map();
Array.from(Array(n), (_, i) => (i + 1).toString()).forEach((num) => {
  const digitOfnumber = num.split("").map(Number);
  digitOfnumber.forEach((n) => {
    const prev = digitCounter.get(n);
    if (prev) {
      digitCounter.set(n, prev + 1);
      return;
    }

    digitCounter.set(n, 1);
  });
});

console.log(digitCounter.get(d));
