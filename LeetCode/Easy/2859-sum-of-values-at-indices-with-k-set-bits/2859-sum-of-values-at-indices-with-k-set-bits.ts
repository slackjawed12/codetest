function sumIndicesWithKSetBits(nums: number[], k: number): number {
  const countBit = (x: number) => {
    let count = 0;
    while (x !== 0) {
      count += x & 1;
      x = x >> 1;
    }
    return count;
  };

  const indexSum = nums
    .filter((_, index) => countBit(index) === k)
    .reduce((acc, cur) => (acc += cur), 0);

  return indexSum;
}
