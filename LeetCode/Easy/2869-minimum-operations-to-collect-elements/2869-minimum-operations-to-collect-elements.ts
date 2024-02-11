function minOperations(nums: number[], k: number): number {
  const lastIndices = nums.reduce((prev, cur, index) => {
    const item = prev.get(cur);
    prev.set(cur, item ? Math.max(index, item) : index);
    return prev;
  }, new Map());

  const info = Array.from(lastIndices);
  info.sort((o1, o2) => o1[0] - o2[0]);
  const answer = info.reduce((prev, cur) => {
    if (cur[0] <= k) {
      return Math.max(prev, nums.length - cur[1]);
    }
    return prev;
  }, 0);
  return answer;
}
