function minOperations(nums: number[], k: number): number {
  nums.sort((o1, o2) => o1 - o2);
  let low = 0;
  let high = nums.length - 1;
  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    if (nums[mid] >= k) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  return low;
}
