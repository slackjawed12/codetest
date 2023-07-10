const fs = require("fs");
const [n, ...input] = fs.readFileSync("/dev/stdin").toString().split("\n");

const solution = (list) => {
  const store = new Map(
    list.map((x) => {
      const info = x.split(" ");
      return [info[0], info[1]];
    })
  );

  let result = [];
  for (const e of store.entries()) {
    if (e[1] === "enter") {
      result.push(e[0]);
    }
  }
  return result.sort((a, b) => (a > b ? -1 : 1));
};

console.log(solution(input).join("\n"));
