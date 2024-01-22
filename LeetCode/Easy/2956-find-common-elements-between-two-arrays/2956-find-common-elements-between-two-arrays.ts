function findIntersectionValues(nums1: number[], nums2: number[]): number[] {
  const [store1, store2] = [new Set(nums1), new Set(nums2)];
  const countArr = (arr: number[], store: Set<number>) =>
    arr.reduce((acc, cur) => (acc += store.has(cur) ? 1 : 0), 0);
  return [countArr(nums1, store2), countArr(nums2, store1)];
}
