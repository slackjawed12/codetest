import fs = require("fs");

const N = parseInt(fs.readFileSync("/dev/stdin").toString().trim());

let cur = N;
let answer = 0;
while (cur > 0) {
  let e = 1;
  while (Math.floor((e * (e + 1)) / 2) <= cur) {
    e++;
  }

  cur -= Math.floor(((e - 1) * e) / 2);
  answer += e - 1;
}

console.log(answer);
