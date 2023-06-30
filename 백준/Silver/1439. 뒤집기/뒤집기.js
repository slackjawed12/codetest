var readline = require("readline");
var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
var solution = function (S) {
  let total = 0;
  S.split("").reduce((acc, cur) => {
    total += acc ^ cur;
    return cur;
  });
  return Math.floor((total + 1) / 2);
};
var input = [];
rl.on("line", function (line) {
  return input.push(line.split(" "));
}).on("close", function () {
  var S = input.flat().at(0);
  var answer = solution(S);
  console.log(answer);
  process.exit();
});
