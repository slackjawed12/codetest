const rope = () => {
  let input = require("fs")
    .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n")
    .map(Number);
  const len = input[0];
  let max = -1;
  input.shift();
  input.sort((a, b) => a - b);
  for (let i = 0; i < len; i++) {
    if (max < input[i] * (len - i)) max = input[i] * (len - i);
  }
  console.log(max);
};

rope();