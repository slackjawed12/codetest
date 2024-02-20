function countKeyChanges(s: string): number {
  const arr = s.split("");
  return arr.reduce((acc, cur, index) => {
    if (index === 0) {
      return acc;
    }
    const prev = arr[index - 1];
    return (acc += cur.toLowerCase() !== prev.toLowerCase() ? 1 : 0);
  }, 0);
}
