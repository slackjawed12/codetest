function findPeaks(mountain: number[]): number[] {
  return mountain.reduce<number[]>((prev, cur, index) => {
    if (index === 0 || index === mountain.length - 1) {
      return prev;
    }
    if (cur > mountain[index - 1] && cur > mountain[index + 1]) {
      prev.push(index);
    }
    return prev;
  }, []);
}
