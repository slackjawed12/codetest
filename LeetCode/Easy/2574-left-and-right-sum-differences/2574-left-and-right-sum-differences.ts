function leftRightDifference(nums: number[]): number[] {
  const leftSum = [0];
  const rightSum = [0];
  const len = nums.length;
  for (let i = 0; i < len - 1; i++) {
    leftSum.push(nums[i] + leftSum[i]);
    rightSum.push(nums[len - i - 1] + rightSum[i]);
  }

  return Array.from(Array(nums.length), (_, i) =>
    Math.abs(leftSum[i] - rightSum[len - i - 1])
  );
}
