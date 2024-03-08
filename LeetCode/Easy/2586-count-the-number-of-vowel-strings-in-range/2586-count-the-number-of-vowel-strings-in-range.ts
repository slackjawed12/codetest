function vowelStrings(words: string[], left: number, right: number): number {
  const vowels = new Set("aeiou".split(""));
  return words
    .slice(left, right + 1)
    .filter((word) => vowels.has(word[0]) && vowels.has(word[word.length - 1]))
    .length;
}
