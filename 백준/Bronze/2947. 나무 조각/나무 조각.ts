import fs = require("fs");

const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let isSorted = false;
while (!isSorted) {
  for (let i = 0; i < input.length - 1; i++) {
    if (input[i] > input[i + 1]) {
      const temp = input[i];
      input[i] = input[i + 1];
      input[i + 1] = temp;
      console.log(input.join(" "));
    }
  }

  let t = true;
  for (let i = 0; i < input.length - 1; i++) {
    t &&= input[i] < input[i + 1] ? true : false;
  }
  isSorted = t;
}
