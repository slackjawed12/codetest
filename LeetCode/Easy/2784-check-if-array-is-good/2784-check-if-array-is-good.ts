function isGood(nums: number[]): boolean {
  nums.sort((o1, o2) => o1 - o2);
  const maxNum = nums.length - 1;
  if (nums[nums.length - 1] !== maxNum) {
    return false;
  }
  nums.pop();

  let order = 1;
  for (const num of nums) {
    if (num !== order) {
      return false;
    }
    order += 1;
  }

  return true;
}
