const readline = require("readline");
const { stdin, stdout } = process;
const rl = readline.createInterface({
  input: stdin,
  output: stdout,
});

const solution = (A, B) => {
  const { sumA, sumB } = A.reduce(
    (acc, cur, i) => {
      if (cur < B[i]) {
        acc.sumB += 3;
      } else if (cur > B[i]) {
        acc.sumA += 3;
      } else {
        acc.sumB += 1;
        acc.sumA += 1;
      }
      return acc;
    },
    { sumA: 0, sumB: 0 }
  );

  let l = A.length - 1;
  while (A[l] === B[l] && l >= 0) {
    l--;
  }

  const lastWinner = l === -1 ? "D" : A[l] > B[l] ? "A" : "B";
  const winner = sumA === sumB ? lastWinner : sumA > sumB ? "A" : "B";
  return { sumA: sumA, sumB: sumB, winner: winner };
};

const input = [];
rl.on("line", function (line) {
  input.push(line.split(" "));
}).on("close", function () {
  const [A, B] = input.map((e) => e.map((n) => parseInt(n)));
  const answer = solution(A, B);
  console.log(answer.sumA, answer.sumB);
  console.log(answer.winner);
  process.exit();
});
