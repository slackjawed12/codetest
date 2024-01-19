function maxFrequencyElements(nums: number[]): number {
  const frequencies = nums.reduce((prev, cur) => {
    prev.set(cur, prev.get(cur) ? prev.get(cur) + 1 : 1);
    return prev;
  }, new Map());

  const maxFreq = Array.from(frequencies).reduce(
    (acc, cur) => (acc = Math.max(acc, cur[1])),
    0
  );
  return Array.from(frequencies).reduce(
    (acc, cur) => (acc += cur[1] === maxFreq ? cur[1] : 0),
    0
  );
}
