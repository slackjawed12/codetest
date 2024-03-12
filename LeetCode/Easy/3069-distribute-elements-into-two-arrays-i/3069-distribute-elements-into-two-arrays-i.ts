function resultArray(nums: number[]): number[] {
  const result = nums.slice(2).reduce(
    (prev, cur) => {
      if (prev.arr1[prev.arr1.length - 1] > prev.arr2[prev.arr2.length - 1]) {
        prev.arr1.push(cur);
      } else {
        prev.arr2.push(cur);
      }
      return prev;
    },
    { arr1: [nums[0]], arr2: [nums[1]] }
  );

  return [...result.arr1, ...result.arr2];
}
