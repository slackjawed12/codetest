function incremovableSubarrayCount(nums: number[]): number {
  let count = 0;
  for (let i = 1; i <= nums.length; i++) {
    for (let start = 0; start <= nums.length - i; start++) {
      const rem = nums.filter(
        (v, index) => index < start || index >= start + i
      );
      count += isStrictlyIncreasing(rem) ? 1 : 0;
    }
  }
  return count;
}

function isStrictlyIncreasing(arr: number[]): boolean {
  for (let i = 0; i < arr.length - 1; i++) {
    if (arr[i] >= arr[i + 1]) {
      return false;
    }
  }

  return true;
}
