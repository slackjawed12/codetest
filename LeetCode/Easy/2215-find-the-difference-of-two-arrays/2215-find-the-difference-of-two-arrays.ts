function findDifference(nums1: number[], nums2: number[]): number[][] {
  const answer: number[][] = [[], []];
  const [store1, store2] = [new Set(nums1), new Set(nums2)];
  Array.from(store1).forEach((val) => {
    if (!store2.has(val)) {
      answer[0].push(val);
    }
  });

  Array.from(store2).forEach((val) => {
    if (!store1.has(val)) {
      answer[1].push(val);
    }
  });

  return answer;
}
