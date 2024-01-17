function twoOutOfThree(
  nums1: number[],
  nums2: number[],
  nums3: number[]
): number[] {
  const reduceToSet = (arr: number[]) => {
    return arr.reduce((prev, cur) => {
      prev.add(cur);
      return prev;
    }, new Set());
  };
  const [first, second, third] = [
    reduceToSet(nums1),
    reduceToSet(nums2),
    reduceToSet(nums3),
  ];
  const distinct = new Set([...nums1, ...nums2, ...nums3]);
  const result = Array.from(distinct).reduce((prev: number[], cur) => {
    if (first.has(cur) && second.has(cur)) {
      prev.push(cur);
    } else if (first.has(cur) && third.has(cur)) {
      prev.push(cur);
    } else if (second.has(cur) && third.has(cur)) {
      prev.push(cur);
    }

    return prev;
  }, []);

  return result;
}
