function numOfStrings(patterns: string[], word: string): number {
  return patterns.reduce(
    (prev, cur) => (prev += word.includes(cur) ? 1 : 0),
    0
  );
}
