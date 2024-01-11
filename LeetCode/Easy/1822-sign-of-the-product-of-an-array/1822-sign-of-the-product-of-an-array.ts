function arraySign(nums: number[]): number {
  let answer = 1;
  for (const num of nums) {
    if (num === 0) {
      return 0;
    }
    if (num < 0) {
      answer *= -1;
    }
  }

  return answer;
}
