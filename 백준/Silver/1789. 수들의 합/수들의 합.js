const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (S) => {
  let answer = 1;
  while (S >= (answer * (answer + 1)) / 2) {
    answer++;
  }
  return answer - 1;
};

let input;
rl.on("line", function (line) {
  input = line;
}).on("close", function () {
  const S = parseInt(input);
  const answer = solution(S);
  console.log(answer);
  process.exit();
});
