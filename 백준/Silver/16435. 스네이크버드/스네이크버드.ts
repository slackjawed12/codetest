import { readFileSync } from "fs";

const [num, input] = readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, L] = num.split(" ").map(Number);
const heights = input.split(" ").map(Number);

const result = heights
  .sort((x, y) => x - y)
  .reduce((acc, cur) => {
    acc += cur <= acc ? 1 : 0;
    return acc;
  }, L);

console.log(result);
