function findWordsContaining(words: string[], x: string): number[] {
  return words
    .map((w, i) => {
      return w.indexOf(x) === -1 ? -1 : i;
    })
    .filter((i) => i !== -1);
}
