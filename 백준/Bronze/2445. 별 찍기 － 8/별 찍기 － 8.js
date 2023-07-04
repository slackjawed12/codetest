const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (N) => {
  return Array.from(Array(2 * N - 1), (_) => "").map((e, i) => {
    const star = "*".repeat(N - Math.abs(i - N + 1));
    const space = " ".repeat(Math.abs(2 * N - 2 * i - 2));
    return star.concat(space).concat(star);
  });
};

let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const N = parseInt(input.pop());
  const answer = solution(N);
  answer.forEach((row) => {
    console.log(row);
  });
  process.exit();
});