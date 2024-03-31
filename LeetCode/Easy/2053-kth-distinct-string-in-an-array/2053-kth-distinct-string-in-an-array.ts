function kthDistinct(arr: string[], k: number): string {
  const store = arr.reduce((acc, cur, index) => {
    const prev = acc.get(cur);
    acc.set(cur, {
      index,
      count: prev ? prev.count + 1 : 1,
    });
    return acc;
  }, new Map());

  const l = Array.from(store).filter((entry) => entry[1].count === 1);
  l.sort((o1, o2) => o1[1].index - o2[1].index);
  if (k <= l.length) {
    return l[k - 1][0];
  }

  return "";
}
