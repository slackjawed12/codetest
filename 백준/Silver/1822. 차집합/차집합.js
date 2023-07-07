const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (A, B) => {
  let answer = [];
  let i = 0;
  let j = 0;
  while (i < A.length && j < B.length) {
    if (A[i] < B[j]) {
      answer.push(A[i]);
      i++;
    } else if (A[i] > B[j]) {
      j++;
    } else {
      i++;
      j++;
    }
  }

  while (i < A.length) {
    answer.push(A[i]);
    i++;
  }

  return answer;
};

let input = [];
rl.on("line", function (line) {
  input.push(line.split(" "));
}).on("close", function () {
  const [n, A, B] = input;
  const answer = solution(
    A.map(Number).sort((x, y) => x - y),
    B.map(Number).sort((x, y) => x - y)
  );
  console.log(answer.length);
  if (answer.length !== 0) {
    console.log(...answer);
  }
  process.exit();
});
