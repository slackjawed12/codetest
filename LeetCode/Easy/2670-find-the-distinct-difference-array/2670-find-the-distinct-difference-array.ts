function distinctDifferenceArray(nums: number[]): number[] {
  const answer = nums.map((num, index) => {
    const prefix = new Set(nums.slice(0, index + 1));
    const suffix = new Set(nums.slice(index + 1));
    return prefix.size - suffix.size;
  });

  return answer;
}
