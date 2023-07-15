import fs = require("fs");
const input = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const odds = input.filter((val) => val % 2);
const sum = odds.reduce((acc, cur) => (acc += cur), 0);
const min = odds.reduce((prev, cur) => Math.min(cur, prev), Infinity);
if(odds.length===0){
    console.log(-1);
} else{
    console.log([sum, min].join("\n"));   
}
