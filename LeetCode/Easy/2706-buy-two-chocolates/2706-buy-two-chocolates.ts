function buyChoco(prices: number[], money: number): number {
  prices.sort((o1, o2) => o1 - o2);
  const minSum = prices[0] + prices[1];
  return minSum > money ? money : money - minSum;
}
