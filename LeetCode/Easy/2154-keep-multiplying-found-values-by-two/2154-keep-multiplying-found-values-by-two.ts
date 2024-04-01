function findFinalValue(nums: number[], original: number): number {
  let cur = original;
  while (true) {
    const idx = nums.indexOf(cur);
    if (idx === -1) {
      break;
    } else {
      cur *= 2;
    }
  }

  return cur;
}
