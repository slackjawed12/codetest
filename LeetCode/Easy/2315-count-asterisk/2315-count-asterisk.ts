function countAsterisks(s: string): number {
  const words = s.split("|");

  const consideredWords = words.filter((w, i) => i % 2 === 0);

  return consideredWords.reduce((prev, cur) => {
    const countAsterisk = cur.split("").reduce((acc, cur) => {
      return (acc += cur === "*" ? 1 : 0);
    }, 0);
    prev += countAsterisk;
    return prev;
  }, 0);
}
