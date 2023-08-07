const fs = require("fs");

const [N, target, ...input] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const countWord = (word) => {
  return word.split("").reduce((prev, cur) => {
    const count = prev.get(cur);

    prev.set(cur, count ? count + 1 : 1);

    return prev;
  }, new Map());
};

const counts = input
  .map((word) => {
    return countWord(word);
  })
  .reduce((prev, cur) => {
    for (const ch of target.split("")) {
      const cnt = cur.get(ch);
      cur.set(ch, cnt ? cnt - 1 : -1);
    }
    const diffs = Array.from(cur.values()).filter((v) => v !== 0);
    if (diffs.find((v) => Math.abs(v) >= 2) >= 0) {
      return prev;
    } else {

      if (diffs.length === 0) {
        return prev + 1;
      }
      const surplus = diffs.filter((v) => v === 1);
      const lack = diffs.filter((v) => v === -1);

      if (surplus.length === 1 && lack.length === 0) {
        return prev + 1;
      }

      if (lack.length === 1 && surplus.length === 0) {
        return prev + 1;
      }

      if (lack.length === 1 && surplus.length === 1) {
        return prev + 1;
      }
    }
    return prev;
  }, 0);

console.log(counts);
