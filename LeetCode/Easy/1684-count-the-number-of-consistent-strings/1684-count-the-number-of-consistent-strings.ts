function countConsistentStrings(allowed: string, words: string[]): number {
  const set = new Set(allowed.split(""));
  return words.filter(
    (w) => w.split("").filter((c) => !set.has(c)).length === 0
  ).length;
}
