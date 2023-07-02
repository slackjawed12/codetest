const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (input) => {
  let matrix = Array.from(Array(101), (_) => Array.from(Array(101), (_) => 0));
  input.forEach((rectangle) => {
    let [xi, yi, xf, yf] = rectangle;
    for (let i = yi; i < yf; i++) {
      for (let j = xi; j < xf; j++) {
        matrix[i][j] = 1;
      }
    }
  });

  let answer = matrix
    .map((array) => {
      return array.reduce((prev, cur) => prev + cur, 0);
    })
    .reduce((acc, cur) => acc + cur, 0);
  return answer;
};

let input = [];
rl.on("line", function (line) {
  input.push(line.split(" "));
}).on("close", function () {
  const nums = input.map((arr) => {
    return arr.map((e) => parseInt(e));
  });
  const answer = solution(nums);
  console.log(answer);
  process.exit();
});
