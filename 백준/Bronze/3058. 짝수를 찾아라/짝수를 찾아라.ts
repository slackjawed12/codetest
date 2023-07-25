import fs = require("fs");

const [T, ...cases] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((row) => row.split(" "))
  .map((r) => r.map(Number));

const result = cases.map((c) => {
  const evenNumbers = c.filter((val) => !(val % 2));
  return [
    evenNumbers.reduce((acc, cur) => (acc += cur), 0),
    evenNumbers.reduce((prev, cur) => (prev = Math.min(prev, cur)), Infinity),
  ];
});

console.log(result.map((r) => r.join(" ")).join("\n"));
