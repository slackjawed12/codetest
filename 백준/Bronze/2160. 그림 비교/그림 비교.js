const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().split("\n");
const N = parseInt(input[0]);
const arr = [];
for (let i = 1; i <= N; i++) {
  arr.push(input.slice(1 + 5 * (i - 1), 1 + 5 * i));
}

let answer = [];
let min = Infinity;
let temp = 0;
for (let i = 0; i < N - 1; i++) {
  const first = arr[i];
  for (let j = i + 1; j < N; j++) {
    const second = arr[j];
    for (let y = 0; y < 5; y++) {
      for (let x = 0; x < 7; x++) {
        if (first[y][x] !== second[y][x]) {
          temp++;
        }
      }
    }
    if (min > temp) {
      answer = [i + 1, j + 1];
      min = temp;
    }
    temp = 0;
  }
}

console.log(answer[0], answer[1]);