const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (N) => {
  for (let i = 0; i < 2 * N - 1; i++) {
    const count = i <= N - 1 ? 2 * N - (2 * i + 1) : 2 * i + 3 - 2 * N;
    const space = " ".repeat(Math.floor((2 * N - 1 - count) / 2));
    const star = "*".repeat(count);
    console.log(space.concat(star));
  }
};

let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  solution(parseInt(input[0]));
  process.exit();
});
