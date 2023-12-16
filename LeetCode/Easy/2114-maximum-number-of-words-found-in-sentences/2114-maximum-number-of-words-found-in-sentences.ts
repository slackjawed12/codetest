function mostWordsFound(sentences: string[]): number {
  return sentences.reduce((prev, cur) => {
    const wordCount = cur.split(" ").length;
    return (prev = Math.max(prev, wordCount));
  }, 0);
}
