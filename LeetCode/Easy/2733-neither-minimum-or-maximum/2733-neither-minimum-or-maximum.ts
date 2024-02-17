function findNonMinOrMax(nums: number[]): number {
  if (nums.length <= 2) {
    return -1;
  }

  nums.sort((o1, o2) => o1 - o2);
  return nums[1];
}
