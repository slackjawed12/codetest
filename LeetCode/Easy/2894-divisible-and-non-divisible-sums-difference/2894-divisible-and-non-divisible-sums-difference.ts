function differenceOfSums(n: number, m: number): number {
  const total = (n * (n + 1)) / 2;
  const count = Math.floor(n / m);
  const num2 = (m * count * (count + 1)) / 2;
  const num1 = total - num2;
  return num1 - num2;
}
