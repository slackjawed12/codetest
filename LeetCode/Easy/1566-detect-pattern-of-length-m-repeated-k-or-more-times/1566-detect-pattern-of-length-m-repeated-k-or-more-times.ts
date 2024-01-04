function containsPattern(arr: number[], m: number, k: number): boolean {
  const isTwoArrayEqual = (a: number[], b: number[]) => {
    if (a.length !== b.length) {
      return false;
    }
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) {
        return false;
      }
    }
    return true;
  };

  for (let i = 0; i < arr.length - m + 1; i++) {
    const pattern = arr.slice(i, i + m);
    let repeat = 1;
    for (let j = i + m; j < arr.length; j += m) {
      const comp = arr.slice(j, j + m);
      const isEqual = isTwoArrayEqual(pattern, comp);
      if (!isEqual) {
        break;
      }
      repeat++;
    }

    if (repeat >= k) {
      return true;
    }
  }
  return false;
}
