function maximizeSum(nums: number[], k: number): number {
  const max = Math.max(...nums);
  return k * max + (k * (k - 1)) / 2;
}
