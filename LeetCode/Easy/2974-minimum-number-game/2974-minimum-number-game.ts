function numberGame(nums: number[]): number[] {
  const arr: number[] = [];
  nums.sort((o1, o2) => o2 - o1);
  while (nums.length !== 0) {
    const a = nums.pop();
    const b = nums.pop();
    arr.push(b!);
    arr.push(a!);
  }

  return arr;
}
