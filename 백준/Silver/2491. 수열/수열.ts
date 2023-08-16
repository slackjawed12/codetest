import fs = require("fs");

const [N, input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const arr = input.split(" ").map(Number);
const inc = [0, 1];
const dec = [0, 1];
for (let i = 1; i < arr.length; i++) {
  if (arr[i - 1] === arr[i]) {
    inc.push(inc[inc.length - 1] + 1);
    dec.push(dec[dec.length - 1] + 1);
  } else if (arr[i - 1] > arr[i]) {
    dec.push(dec[dec.length - 1] + 1);
    inc.push(1);
  } else {
    inc.push(inc[inc.length - 1] + 1);
    dec.push(1);
  }
}

const answer = [...inc, ...dec].reduce((prev, cur) => Math.max(prev, cur), 0);

console.log(answer);
