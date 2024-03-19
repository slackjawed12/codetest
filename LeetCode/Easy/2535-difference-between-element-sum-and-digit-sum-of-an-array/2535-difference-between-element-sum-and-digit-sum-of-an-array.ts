function differenceOfSum(nums: number[]): number {
  const result = nums.reduce(
    (prev, cur) => {
      prev.elemSum += cur;
      prev.digitSum += cur
        .toString()
        .split("")
        .reduce((acc, cur) => (acc += parseInt(cur)), 0);
      return prev;
    },
    { elemSum: 0, digitSum: 0 }
  );

  return Math.abs(result.elemSum - result.digitSum);
}
