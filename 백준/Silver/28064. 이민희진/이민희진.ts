import fs = require("fs");

const [N, ...names] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const getPrefixAndSuffix = (name: string) => {
  return Array.from(Array(name.length), (_, i) => {
    return {
      prefix: name.slice(0, i + 1),
      suffix: name.slice(-i - 1),
    };
  });
};
const result = names.reduce((acc, cur, index) => {
  const targets = names.slice(index + 1);

  const presuf = getPrefixAndSuffix(cur);

  const count = targets.reduce((a, c) => {
    const canlink =
      presuf.filter((ps) => c.startsWith(ps.suffix) || c.endsWith(ps.prefix))
        .length > 0;
    return (a += canlink ? 1 : 0);
  }, 0);

  return (acc += count);
}, 0);

console.log(result);
