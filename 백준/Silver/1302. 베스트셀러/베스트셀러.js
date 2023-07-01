const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (titles) => {
  let group = titles.reduce((acc, cur) => {
    const title = cur;
    if (acc[title]) {
      acc[title] += 1;
    } else {
      acc[title] = 1;
    }
    return acc;
  }, {});
  const most = Object.values(group).reduce((acc, cur) => Math.max(acc, cur), 0);
  return Object.entries(group)
    .filter((x) => x[1] === most)
    .map((x) => x[0])
    .sort()
    .slice(0, 1);
};

let input = [];
rl.on("line", function (line) {
  input.push(line.split(" "));
}).on("close", function () {
  const [N, ...titles] = input.flat();
  const answer = solution(titles);

  answer.forEach((x) => console.log(x));
  process.exit();
});
