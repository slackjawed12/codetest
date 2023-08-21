import fs = require("fs");

const N = parseInt(fs.readFileSync("/dev/stdin").toString().trim());

const queue = Array.from(Array(N), (_, i) => i + 1);

const stack = [];

while (queue.length > 0) {
  stack.push(queue.shift());

  if (queue.length === 0) break;
  queue.push(queue.shift() ?? 0);
}

console.log(stack.join(" "));
