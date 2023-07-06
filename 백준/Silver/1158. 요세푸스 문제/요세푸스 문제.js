const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (N, K) => {
  const source = Array.from(Array(N), (_, i) => i + 1);

  let answer = [];
  let count = 1;
  while (answer.length != N) {
    const x = source.shift();
    if (count !== K) {
      source.push(x);
      count++;
    } else {
      answer.push(x);
      count = 1;
    }
  }
  return answer.reduce((acc, cur, i) => {
    if (i !== N - 1) {
      return acc + cur + ", ";
    } else {
      return acc + cur + ">";
    }
  }, "<");
};

let input = [];
rl.on("line", function (line) {
  input.push(line.split(" "));
}).on("close", function () {
  const [N, K] = input.flat().map((x) => parseInt(x));
  const answer = solution(N, K);

  console.log(answer);
  process.exit();
});
