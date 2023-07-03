const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = (source, query) => {
  let count = 0;
  while (source != "") {
    const index = source.indexOf(query);
    if (index >= 0) {
      count += 1;
      source = source.slice(index + query.length);
    } else {
      break;
    }
  }
  return count;
};

let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  const [source, query] = input;
  const answer = solution(source, query);
  console.log(answer);
  process.exit();
});
