function halvesAreAlike(s: string): boolean {
  const vowels = new Set(["a", "e", "i", "o", "u"]);
  let countA = 0;
  let countB = 0;
  const lower = s.toLowerCase();
  for (let i = 0; i < lower.length; i++) {
    if (i < lower.length / 2) {
      countA = vowels.has(lower[i]) ? countA + 1 : countA;
    } else {
      countB = vowels.has(lower[i]) ? countB + 1 : countB;
    }
  }

  return countA === countB;
}
