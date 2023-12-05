function countGoodSubstrings(s: string): number {
  const hasRepeatedCharacters = (str: string) => {
    const store = str.split("").reduce((prev, cur) => {
      if (!prev.has(cur)) {
        prev.add(cur);
      }
      return prev;
    }, new Set());
    return store.size !== str.length;
  };

  const getSubstrings = (str: string) => {
    if (str.length <= 2) {
      return [];
    }

    return Array.from(Array(str.length - 2), (_, i) => str.slice(i, i + 3));
  };

  return getSubstrings(s).filter((sub) => !hasRepeatedCharacters(sub)).length;
}
