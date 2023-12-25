function maximumWealth(accounts: number[][]): number {
  return accounts.reduce((acc, cur) => {
    const currentWealth = cur.reduce((p, money) => (p += money), 0);
    return Math.max(acc, currentWealth);
  }, 0);
}
