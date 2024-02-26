function getLongestSubsequence(words: string[], groups: number[]): string[] {
  const answer: string[] = [];
  answer.push(words[0]);
  for (let i = 0; i < words.length - 1; i++) {
    if (groups[i] !== groups[i + 1]) {
      answer.push(words[i + 1]);
    }
  }

  return answer;
}
