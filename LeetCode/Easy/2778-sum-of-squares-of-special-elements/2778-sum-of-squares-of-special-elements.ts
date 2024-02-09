function sumOfSquares(nums: number[]): number {
  return nums.reduce((acc, cur, index) => {
    if (nums.length % (index + 1) === 0) {
      acc += cur ** 2;
    }

    return acc;
  }, 0);
}
