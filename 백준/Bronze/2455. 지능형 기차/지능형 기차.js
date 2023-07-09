const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  const answer = input
    .map((i) => {
      const info = i.split(" ");
      const outNum = -info[0];
      const inNum = +info[1];
      return inNum + outNum;
    })
    .reduce((prev, cur) => {
      prev.push((prev[prev.length - 1] ?? 0) + cur);
      return prev;
    }, [])
    .reduce((acc, cur) => (acc > cur ? acc : cur), 0);

  return answer;
};

let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const answer = solution(input);
  console.log(answer);
  process.exit();
});
