function areOccurrencesEqual(s: string): boolean {
  const countStore = s.split("").reduce((prev, cur) => {
    const elem = prev.get(cur);
    prev.set(cur, elem ? elem + 1 : 1);
    return prev;
  }, new Map());

  const array = Array.from(countStore);
  return array.reduce(
    (prev, cur) => {
      prev[0] &&= cur[1] === prev[1];
      return prev;
    },
    [true, array[0][1]]
  )[0];
}
