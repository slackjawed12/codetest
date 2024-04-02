function minBitFlips(start: number, goal: number): number {
  let not = start ^ goal;
  let answer = 0;
  while (not) {
    answer += not & 1;
    not = not >>> 1;
  }
  return answer;
}
