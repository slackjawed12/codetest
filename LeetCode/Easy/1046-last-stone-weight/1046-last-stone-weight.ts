function lastStoneWeight(stones: number[]): number {
  const copy = stones.slice();
  while (copy.length !== 1 && copy.length !== 0) {
    copy.sort((o1, o2) => o1 - o2);
    const first = copy.pop() ?? 0;
    const second = copy.pop() ?? 0;
    if (first > second) {
      copy.push(first - second);
    }
  }

  return copy.length === 0 ? 0 : copy[0];
}
