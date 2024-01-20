function hasTrailingZeros(nums: number[]): boolean {
  return nums.filter((n) => n % 2 === 0).length >= 2;
}
