function distributeCandies(n: number, limit: number): number {
  let answer = 0;
  for (let i = 0; i <= limit; i++) {
    for (let j = 0; j <= limit; j++) {
      const k = n - i - j;
      if (k < 0 || k > limit) {
        continue;
      }
      answer += 1;
    }
  }
  return answer;
}
