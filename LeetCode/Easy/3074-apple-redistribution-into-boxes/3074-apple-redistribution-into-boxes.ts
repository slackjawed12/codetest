function minimumBoxes(apple: number[], capacity: number[]): number {
  capacity.sort((o1, o2) => o2 - o1);
  const accCapacity = capacity.reduce<number[]>((prev, cur, idx) => {
    if (idx === 0) {
      prev.push(cur);
    } else {
      prev.push(prev[idx - 1] + cur);
    }
    return prev;
  }, []);

  const appleSum = apple.reduce((acc, cur) => (acc += cur), 0);
  return accCapacity.findIndex((v) => v >= appleSum) + 1;
}
