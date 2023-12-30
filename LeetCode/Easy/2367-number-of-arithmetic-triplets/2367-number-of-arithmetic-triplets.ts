// time complexity : O(n^3), space complexity: O(1)
function arithmeticTriplets(nums: number[], diff: number): number {
  let answer = 0;
  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        if (nums[k] - nums[j] === diff && nums[j] - nums[i] === diff) {
          answer++;
        }
      }
    }
  }

  return answer;
}

// time complexity : O(n), space complexity : O(n)
function arithmeticTripletsV2(nums: number[], diff: number): number {
  let answer = 0;
  const store = new Set();

  for (const num of nums) {
    if (store.has(num - diff) && store.has(num - diff * 2)) {
      answer++;
    }
    store.add(num);
  }

  return answer;
}
