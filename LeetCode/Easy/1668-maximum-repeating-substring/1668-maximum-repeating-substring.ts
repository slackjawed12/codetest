function maxRepeating(sequence: string, word: string): number {
  let answer = 0;
  for (let i = 1; i <= Math.floor(sequence.length / word.length); i++) {
    const curWord = word.repeat(i);
    if (sequence.includes(curWord)) {
      answer = Math.max(answer, i);
    }
  }

  return answer;
}
