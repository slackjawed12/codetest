function semiOrderedPermutation(nums: number[]): number {
  const firstIndex = nums.indexOf(1);
  const lastIndex = nums.indexOf(nums.length);
  const offset = lastIndex > firstIndex ? 0 : 1;
  return firstIndex + (nums.length - lastIndex - 1) - offset;
}
