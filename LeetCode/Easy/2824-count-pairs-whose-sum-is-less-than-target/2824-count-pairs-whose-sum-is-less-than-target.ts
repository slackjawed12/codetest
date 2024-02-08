function countPairs(nums: number[], target: number): number {
  let answer = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] < target) {
        answer += 1;
      }
    }
  }

  return answer;
}
