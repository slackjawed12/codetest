import fs = require("fs");

const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const getCombinationHelper = function <T>({
  source,
  r,
  index,
  cur,
  result,
}: {
  source: T[];
  r: number;
  index: number;
  cur: T[];
  result: T[][];
}) {
  if (r === 0) {
    result.push(cur);
    return;
  }

  for (let i = index; i < source.length - r + 1; i++) {
    const path = Array.from(cur);
    path.push(source[i]);
    getCombinationHelper({
      source,
      index: i + 1,
      r: r - 1,
      cur: path,
      result,
    });
  }
};

const getCombination = function <T>({
  source,
  r,
}: {
  source: T[];
  r: number;
}): T[][] {
  const result: T[][] = [];
  getCombinationHelper({ source, r, cur: [], index: 0, result });
  return result;
};

const combi = getCombination({ source: input, r: 2 });

for (const x of combi) {
  const filtered = input.filter((val) => !x.includes(val));

  const result = filtered.reduce((acc, cur) => (acc += cur), 0);

  if (result === 100) {
    console.log(filtered.sort((x, y) => x - y).join("\n"));
    break;
  }
}
