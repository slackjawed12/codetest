function sumBase(n: number, k: number): number {
  let sum = 0;
  while (n > 0) {
    sum += n % k;
    n = Math.floor(n / k);
  }
  return sum;
}
