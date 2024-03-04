function maximumCount(nums: number[]): number {
  const result = nums.reduce(
    (prev, cur) => {
      if (cur > 0) {
        prev.pos += 1;
      } else if (cur < 0) {
        prev.neg += 1;
      }
      return prev;
    },
    { pos: 0, neg: 0 }
  );

  return Math.max(result.pos, result.neg);
}

function maximumCountV2(nums: number[]): number {
  let low = 0;
  let high = nums.length - 1;
  let mid = -1;
  while (low <= high) {
    mid = Math.floor((low + high) / 2);
    if (nums[mid] > 0) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  let lown = 0;
  let highn = nums.length - 1;
  let midn = -1;
  while (lown <= highn) {
    midn = Math.floor((lown + highn) / 2);
    if (nums[midn] < 0) {
      lown = midn + 1;
    } else {
      highn = midn - 1;
    }
  }
  const positive = nums.length - low;
  const negative = highn + 1;
  return Math.max(positive, negative);
}
