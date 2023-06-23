const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString();
const gcd = function (a, b) {
  if (b == 0) {
    return a;
  }
  return gcd(b, a % b);
};

const lcm = function (a, b) {
  return (a * b) / gcd(a, b);
};

const solution = function (input) {
  const nums = input.split(" ");
  nums.forEach((x) => parseInt(x));

  let sorted = nums.sort();
  let temp = Infinity;
  // 3개에 대해 최소공배수 구하기
  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        temp = Math.min(temp, lcm(lcm(nums[i], nums[j]), nums[k]));
      }
    }
  }
  return temp;
};

let answer = solution(input);

console.log(answer);
