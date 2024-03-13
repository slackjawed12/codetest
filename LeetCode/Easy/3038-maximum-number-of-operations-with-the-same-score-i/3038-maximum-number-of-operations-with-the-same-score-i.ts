function maxOperations(nums: number[]): number {
  const sum = nums[0] + nums[1];
  let cur = sum;
  let count = 1;
  for (let i = 2; i < nums.length - 1; i += 2) {
    cur = nums[i] + nums[i + 1];
    if (sum !== cur) {
      break;
    }
    count += 1;
  }

  return count;
}
