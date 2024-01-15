function secondHighest(s: string): number {
  const numbers = s.split("").reduce((prev, cur) => {
    const isNumeral =
      cur.charCodeAt(0) >= "0".charCodeAt(0) &&
      cur.charCodeAt(0) <= "9".charCodeAt(0);
    if (isNumeral && !prev.has(parseInt(cur))) {
      prev.add(parseInt(cur));
    }
    return prev;
  }, new Set<number>());

  const arr = Array.from(numbers);
  arr.sort((o1, o2) => o1 - o2);

  if (arr.length <= 1) {
    return -1;
  }

  return arr[arr.length - 2];
}
