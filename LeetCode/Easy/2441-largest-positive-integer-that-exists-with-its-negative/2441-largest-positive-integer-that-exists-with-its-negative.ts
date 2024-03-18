function findMaxK(nums: number[]): number {
  const negatives = new Set(nums.filter((val) => val < 0));

  const answer = nums
    .filter((val) => val > 0)
    .reduce((prev, cur) => {
      if (negatives.has(-cur)) {
        prev = Math.max(prev, cur);
      }
      return prev;
    }, -1);

  return answer;
}
