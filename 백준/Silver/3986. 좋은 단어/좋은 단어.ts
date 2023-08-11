import fs = require("fs");

const [N, ...words] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const isGoodWord = (word: string) => {
  const stack: string[] = [];
  return (
    word.split("").reduce((prev: string[], cur) => {
      if (prev.length === 0 || cur !== prev[prev.length - 1]) {
        prev.push(cur);
        return prev;
      }

      prev.pop();
      return prev;
    }, []).length === 0
  );
};

console.log(
  words.reduce((acc, cur) => {
    return (acc += +isGoodWord(cur));
  }, 0)
);
