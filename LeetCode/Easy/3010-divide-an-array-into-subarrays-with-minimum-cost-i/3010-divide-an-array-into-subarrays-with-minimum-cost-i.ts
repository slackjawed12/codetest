function minimumCost(nums: number[]): number {
  let answer = Infinity;
  for (let i = 1; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      const first = nums.slice(0, i);
      const second = nums.slice(i, j);
      const third = nums.slice(j);

      const costSum = first[0] + second[0] + third[0];
      answer = Math.min(answer, costSum);
    }
  }
  return answer;
}
