import fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();
const N = parseInt(input);
const answer = Array.from(Array(2 * N - 1), (_) => "")
  .map((_, i) => {
    const star = N - Math.abs(N - i - 1);
    const space = N - star;
    return " ".repeat(space).concat("*".repeat(star));
  })
  .join("\n");

console.log(answer);
