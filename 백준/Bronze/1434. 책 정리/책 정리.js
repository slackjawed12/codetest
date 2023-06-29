/**
 * 책 정리
 */
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (A, B) => {
  let answer = 0;
  let i = 0;
  let j = 0;
  let cur = A[i];
  while (i != A.length && j != B.length) {
    // cur : 남은 공간
    if (cur >= B[j]) {
      cur -= B[j++];
    } else {
      answer += cur;
      cur = A[++i];
    }
  }

  answer += cur;

  for (i += 1; i < A.length; i++) {
    answer += A[i];
  }
  return answer;
};

let input = [];
rl.on("line", function (line) {
  input.push(line.split(" "));
}).on("close", function () {
  const [N, M] = input[0].map((x) => parseInt(x));
  const A = input[1].map((x) => parseInt(x));
  const B = input[2].map((x) => parseInt(x));
  const answer = solution(A, B);
  console.log(answer);
  process.exit();
});
