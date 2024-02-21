function maxSum(nums: number[]): number {
  let answer = -1;
  const maxDigit = (n: number) => {
    let r = 0;
    while (n > 0) {
      r = Math.max(n % 10, r);
      n = Math.floor(n / 10);
    }
    return r;
  };

  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      const [first, second] = [nums[i], nums[j]];
      if (maxDigit(first) === maxDigit(second)) {
        answer = Math.max(first + second, answer);
      }
    }
  }
  return answer;
}
