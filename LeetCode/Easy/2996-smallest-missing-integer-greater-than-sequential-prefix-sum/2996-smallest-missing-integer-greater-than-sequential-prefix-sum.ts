function missingInteger(nums: number[]): number {
  let sequentialPrefixSum = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] - nums[i - 1] === 1) {
      sequentialPrefixSum += nums[i];
    } else {
      break;
    }
  }

  const store = new Set(nums);
  for (let i = sequentialPrefixSum; i <= 51; i++) {
    if (!store.has(i)) {
      return i;
    }
  }

  return sequentialPrefixSum;
}
