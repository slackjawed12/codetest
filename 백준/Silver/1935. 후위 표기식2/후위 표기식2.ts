import fs = require("fs");

const [N, expr, ...operands] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const exprArray = expr.split("");
const store = new Map(
  Array.from(operands, (_, i) => [
    String.fromCharCode("A".charCodeAt(0) + i),
    operands[i],
  ])
);

const isOperator = (ch: string) => {
  return ch.match(/[*+/-]/);
};

const result = exprArray.reduce((prev, cur) => {
  if (isOperator(cur)) {
    const op1 = prev.pop()!;
    const op2 = prev.pop()!;
    const num1 = store.has(op1) ? parseFloat(store.get(op1)!) : parseFloat(op1);
    const num2 = store.has(op2) ? parseFloat(store.get(op2)!) : parseFloat(op2);
    switch (cur) {
      case "+":
        prev.push((num1 + num2).toString());
        break;
      case "-":
        prev.push((num2 - num1).toString());
        break;
      case "*":
        prev.push((num1 * num2).toString());
        break;
      case "/":
        prev.push((num2 / num1).toString());
        break;
    }
  } else {
    prev.push(cur);
  }

  return prev;
}, [] as string[])[0];

console.log(parseFloat(result).toFixed(2));
