function findGCD(nums: number[]): number {
  const GCD = (a: number, b: number) => {
    if (b === 0) {
      return a;
    }
    return GCD(b, a % b);
  };

  nums.sort((o1, o2) => o1 - o2);
  return GCD(nums[0], nums[nums.length - 1]);
}
