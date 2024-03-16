function longestAlternatingSubarray(nums: number[], threshold: number): number {
  let answer = 0;
  for (let l = 0; l < nums.length; l++) {
    if (nums[l] % 2 !== 0) {
      continue;
    }

    for (let r = l; r < nums.length; r++) {
      const subArray = nums.slice(l, r + 1);
      let result = true;
      for (let i = 0; i < subArray.length - 1; i++) {
        if (subArray[i] % 2 === subArray[i + 1] % 2) {
          result = false;
          break;
        }
      }

      for (let i = 0; i < subArray.length; i++) {
        if (subArray[i] > threshold) {
          result = false;
          break;
        }
      }

      if (result) {
        answer = Math.max(answer, subArray.length);
      }
    }
  }

  return answer;
}
