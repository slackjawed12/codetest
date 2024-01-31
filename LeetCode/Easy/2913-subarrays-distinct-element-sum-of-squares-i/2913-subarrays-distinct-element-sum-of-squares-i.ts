function sumCounts(nums: number[]): number {
  let answer = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = i; j < nums.length; j++) {
      const subArr = nums.slice(i, j + 1);
      const set = subArr.reduce((prev, cur) => {
        prev.add(cur);
        return prev;
      }, new Set<number>());
      const distinct = Array.from(set);
      answer += distinct.length ** 2;
    }
  }

  return answer;
}
