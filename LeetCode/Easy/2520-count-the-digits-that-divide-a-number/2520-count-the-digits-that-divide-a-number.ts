function countDigits(num: number): number {
  let temp = num;
  let answer = 0;
  while (temp > 0) {
    const r = temp % 10;
    answer += num % r === 0 ? 1 : 0;
    temp = Math.floor(temp / 10);
  }

  return answer;
}
