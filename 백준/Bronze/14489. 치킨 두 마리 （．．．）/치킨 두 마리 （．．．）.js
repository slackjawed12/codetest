const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (list) => {
  const A = list[0][0];
  const B = list[0][1];
  const C = list[1][0];
  return C * 2 > A + B ? A + B : A + B - C * 2;
};

let input = [];
let list = [];
rl.on("line", function (line) {
  input.push(line.split(" "));
}).on("close", function () {
  input.forEach((value) => {
    list.push(value.map((x) => parseInt(x)));
  });
  const answer = solution(list);
  console.log(answer);
  process.exit();
});
