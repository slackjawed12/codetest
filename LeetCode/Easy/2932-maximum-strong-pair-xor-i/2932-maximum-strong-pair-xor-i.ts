function maximumStrongPairXor(nums: number[]): number {
  const strongPairs: number[][] = [];
  for (let i = 0; i < nums.length; i++) {
    for (let j = i; j < nums.length; j++) {
      if (Math.abs(nums[i] - nums[j]) <= Math.min(nums[i], nums[j])) {
        strongPairs.push([nums[i], nums[j]]);
      }
    }
  }

  return strongPairs.reduce((prev, cur) => {
    prev = Math.max(prev, cur[0] ^ cur[1]);
    return prev;
  }, 0);
}
