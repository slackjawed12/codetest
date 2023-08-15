import fs = require("fs");

const [N, ...rows] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const cards = rows.map((row) => row.split(" ").map(Number));

const maxDigits = cards.map((card) => {
  let maxDigit = 0;
  for (let i = 0; i < card.length - 1; i++) {
    for (let j = i + 1; j < card.length; j++) {
      const digit =
        card
          .filter((v, index) => index !== i && index !== j)
          .reduce((acc, cur) => (acc += cur), 0) % 10;
      maxDigit = Math.max(maxDigit, digit);
    }
  }
  return maxDigit;
});

let answer = 0;
let maxNum = 0;
for (let i = 0; i < maxDigits.length; i++) {
  if (maxDigits[i] > maxNum) {
    maxNum = maxDigits[i];
    answer = i + 1;
  } else if (maxDigits[i] === maxNum) {
    answer = i + 1;
  }
}

console.log(answer);
