const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const reverseNumber = (num) => {
  let res = 0;
  while (num !== 0) {
    res += num % 10;
    num = Math.floor(num / 10);
    res *= num ? 10 : 1;
  }
  return res;
};

const solution = (X, Y) => {
  let rx = reverseNumber(X);
  let ry = reverseNumber(Y);
  let answer = reverseNumber(rx + ry);
  return answer;
};

let input;
rl.on("line", function (line) {
  input = line.split(" ");
}).on("close", function () {
  const X = parseInt(input[0]);
  const Y = parseInt(input[1]);
  const answer = solution(X, Y);
  console.log(answer);
  process.exit();
});
