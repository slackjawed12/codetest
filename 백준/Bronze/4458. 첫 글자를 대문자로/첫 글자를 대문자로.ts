import fs = require("fs");

const [N, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

console.log(
  input.map((row) =>
    row[0].match(/[a-z]/) ? row[0].toUpperCase().concat(row.slice(1)) : row
  ).join('\n')
);
