import fs = require("fs");

const [N, M, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((row) => row.split(" ").map(Number))
  .reduce((prev, cur) => {
    prev.push(...cur);
    return prev;
  }, []);

input.sort((o1, o2) => o1 - o2);

let i = 0;
let j = input.length - 1;
let answer = 0;

while (i < j) {
  const sum = input[i] + input[j];
  if (sum === M) {
    answer++;
    i++;
    j--;
  } else if (sum > M) {
    j--;
  } else {
    i++;
  }
}
console.log(answer);
