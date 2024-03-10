function splitWordsBySeparator(words: string[], separator: string): string[] {
  return words.reduce<string[]>((acc, cur) => {
    return [...acc, ...cur.split(separator).filter((v) => v.length > 0)];
  }, []);
}
