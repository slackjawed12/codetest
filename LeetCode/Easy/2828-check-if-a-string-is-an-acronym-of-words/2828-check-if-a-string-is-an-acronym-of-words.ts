function isAcronym(words: string[], s: string): boolean {
  const concat = words.reduce((prev, cur) => (prev += cur[0]), "");
  return concat === s;
}
