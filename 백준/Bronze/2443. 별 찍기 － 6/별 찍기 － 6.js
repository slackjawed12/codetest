let fs = require("fs");
let input = +fs.readFileSync('/dev/stdin').toString();
// let input = +fs.readFileSync("test.txt").toString();
for (let i = 0; i < input; i++) {
  console.log(" ".repeat(i) + "*".repeat(input * 2 - i * 2 - 1));
}