const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  let answer = [BigInt(0), BigInt(1)];

  for (let i = 2; i <= input; i++) {
    answer.push(BigInt(answer[i - 2]) + BigInt(answer[i - 1]));
  }

  return answer[input].toString();
};

let input = [];
let list = [];
rl.on("line", function (line) {
  input = line.toString();
}).on("close", function () {
  const answer = solution(input);
  console.log(answer);
  process.exit();
});
