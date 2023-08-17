import fs = require("fs");

const [N, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const mineMap = input.map((row) => row.split(""));
const solveMineMap = (mineMap: string[][]) => {
  const result = Array.from(Array(mineMap.length), (_) =>
    Array.from(Array(mineMap.length), (_) => "")
  );
  const dx = [-1, 0, 1, -1, 1, -1, 0, 1];
  const dy = [-1, -1, -1, 0, 0, 1, 1, 1];

  return result
    .map((row, i) =>
      row
        .map((val, j) => {
          if (mineMap[i][j] !== ".") {
            return "*";
          }

          let sum = 0;
          for (let k = 0; k < 8; k++) {
            const nx = j + dx[k];
            const ny = i + dy[k];

            if (
              ny >= 0 &&
              ny < mineMap.length &&
              nx >= 0 &&
              nx < mineMap[0].length &&
              mineMap[ny][nx] !== "."
            ) {
              sum += parseInt(mineMap[ny][nx]);
            }
          }
          return sum >= 10 ? "M" : sum.toString();
        })
        .join("")
    )
    .join("\n");
};

console.log(solveMineMap(mineMap));
