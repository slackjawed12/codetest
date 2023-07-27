import fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
input.pop();

const isVowel = (c: string) => {
  return c === "a" || c === "e" || c === "i" || c === "o" || c === "u";
};
const rule1 = (password: string) => {
  const vowels = password.split("").filter((c) => isVowel(c));

  return vowels.length !== 0;
};
const rule2 = (password: string) => {
  const characters = password.split("");
  const stack: string[] = [];
  for (const ch of characters) {
    if (stack.length >= 1 && isVowel(stack[stack.length - 1]) !== isVowel(ch)) {
      stack.splice(0);
    }

    stack.push(ch);

    if (stack.length === 3) {
      return false;
    }
  }
  return true;
};
const rule3 = (password: string) => {
  const characters = password.split("");
  const stack: string[] = [];
  for (const ch of characters) {
    if (stack.length >= 1 && stack[stack.length - 1] !== ch) {
      stack.splice(0);
    }

    stack.push(ch);

    if (stack.length === 2 && ch !== "e" && ch !== "o") {
      return false;
    }
  }
  return true;
};

const rules: ((password: string) => boolean)[] = [];
rules.push(rule1, rule2, rule3);

const evaluate = (password: string): boolean => {
  return rules.reduce((acc, cur) => cur(password) && acc, true);
};

const trueSuffix = " is acceptable.";
const falseSuffix = " is not acceptable.";
console.log(
  input
    .map((str) =>
      evaluate(str)
        ? "<" + str + ">" + trueSuffix
        : "<" + str + ">" + falseSuffix
    )
    .join("\n")
);
