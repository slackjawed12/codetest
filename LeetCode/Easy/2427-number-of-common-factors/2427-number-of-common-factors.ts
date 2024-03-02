function commonFactors(a: number, b: number): number {
  let answer = 0;
  const min = Math.min(a, b);
  for (let i = 1; i <= min; i++) {
    if (a % i === 0 && b % i === 0) {
      answer += 1;
    }
  }
  return answer;
}
