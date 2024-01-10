function maxAscendingSum(nums: number[]): number {
  let subArr = [nums[0]];
  let answer = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] < nums[i + 1]) {
      subArr.push(nums[i + 1]);
    } else {
      answer = Math.max(
        subArr.reduce((acc, cur) => (acc += cur), 0),
        answer
      );
      subArr = [nums[i + 1]];
    }
  }
  answer = Math.max(
    subArr.reduce((acc, cur) => (acc += cur), 0),
    answer
  );
  return answer;
}
