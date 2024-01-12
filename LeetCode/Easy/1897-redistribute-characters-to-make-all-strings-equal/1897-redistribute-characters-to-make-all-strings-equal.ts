function makeEqual(words: string[]): boolean {
  if (words.length === 1) {
    return true;
  }

  const store = words.reduce((prev, cur) => {
    cur.split("").forEach((val) => {
      const count = prev.get(val);
      if (count) {
        prev.set(val, count + 1);
      } else {
        prev.set(val, 1);
      }
    });
    return prev;
  }, new Map());

  const array = Array.from(store);
  return array.reduce(
    (prev, cur) => (prev &&= cur[1] % words.length === 0),
    true
  );
}
