function minOperations(nums: number[]): number {
  let count = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    const diff = nums[i] - nums[i + 1];
    if (diff >= 0) {
      nums[i + 1] += diff + 1;
      count += diff + 1;
    }
  }

  return count;
}
