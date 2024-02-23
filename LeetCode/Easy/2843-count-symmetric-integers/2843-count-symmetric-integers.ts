function countSymmetricIntegers(low: number, high: number): number {
  let answer = 0;
  for (let i = low; i <= high; i++) {
    const digits = i.toString().split("");
    if (digits.length % 2 !== 0) {
      continue;
    }

    const firstHalf = digits.slice(0, Math.floor(digits.length / 2));
    const lastHalf = digits.slice(Math.floor(digits.length / 2));

    const firstSum = firstHalf.reduce((acc, cur) => (acc += parseInt(cur)), 0);
    const lastSum = lastHalf.reduce((acc, cur) => (acc += parseInt(cur)), 0);

    if (firstSum === lastSum) {
      answer += 1;
    }
  }

  return answer;
}
