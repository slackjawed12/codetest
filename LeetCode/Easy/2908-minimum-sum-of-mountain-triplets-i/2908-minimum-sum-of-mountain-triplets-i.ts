function minimumSum(nums: number[]): number {
  let answer = -1;
  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        if (nums[i] < nums[j] && nums[j] > nums[k]) {
          const sum = nums[i] + nums[j] + nums[k];
          answer = answer === -1 ? sum : Math.min(answer, sum);
        }
      }
    }
  }

  return answer;
}
