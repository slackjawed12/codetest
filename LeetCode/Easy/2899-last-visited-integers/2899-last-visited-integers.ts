function lastVisitedIntegers(words: string[]): number[] {
  const answer: number[] = [];
  const stack: number[] = [];
  let i = 0;
  while (i < words.length) {
    if (words[i] !== "prev") {
      stack.push(parseInt(words[i]));
      i++;
    } else {
      const temp = stack.slice();
      while (words[i] === "prev") {
        if (temp.length !== 0) {
          answer.push(temp.pop()!);
        } else {
          answer.push(-1);
        }
        i++;
      }
    }
  }

  return answer;
}
