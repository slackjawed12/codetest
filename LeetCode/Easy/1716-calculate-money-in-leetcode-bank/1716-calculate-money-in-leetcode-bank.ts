function totalMoney(n: number): number {
  const [div, mod] = [Math.floor(n / 7), n % 7];
  const sumQ = ((7 * 4 + 7 * (3 + div)) * div) / 2;
  const sumR = Math.floor(((div + 1 + div + mod) * mod) / 2);
  return sumQ + sumR;
}
