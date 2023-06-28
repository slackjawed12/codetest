const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (arr) => {
  let answer;
  let len = arr[0];
  let avg = arr.slice(1).reduce((x, y) => x + y, 0) / len;
  answer = arr.slice(1).filter((x) => x > avg).length / len;
  return (answer * 100 + Number.EPSILON).toPrecision(5) + "%";
};

let input = [];
let list = [];
rl.on("line", function (line) {
  input.push(line.split(" "));
}).on("close", function () {
  const T = +input[0][0];
  let answer = [];
  for (let i = 0; i < T; i++) {
    const numArr = input[i + 1].map((x) => +x);
    answer.push(solution(numArr));
  }
  answer.forEach((x) => console.log(x));
  process.exit();
});
