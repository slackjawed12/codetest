function similarPairs(words: string[]): number {
  let answer = 0;
  for (let i = 0; i < words.length - 1; i++) {
    for (let j = i + 1; j < words.length; j++) {
      const uniq = Array.from(new Set(words[i].split("")));
      uniq.sort();
      const counter = uniq.join("");
      const uniq2 = Array.from(new Set(words[j].split("")));
      uniq2.sort();
      const counter2 = uniq2.join("");

      answer += counter === counter2 ? 1 : 0;
    }
  }
  return answer;
}
