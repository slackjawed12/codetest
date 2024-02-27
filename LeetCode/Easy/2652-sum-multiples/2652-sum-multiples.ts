function sumOfMultiples(n: number): number {
  return Array.from(Array(n), (_, i) => i + 1).reduce((acc, cur) => {
    if (cur % 3 === 0 || cur % 5 === 0 || cur % 7 === 0) {
      acc += cur;
    }
    return acc;
  }, 0);
}
