function findChampion(grid: number[][]): number {
  let answer = 0;
  let prev = 0;
  for (let i = 0; i < grid.length; i++) {
    const row = grid[i];
    const sum = row.reduce((acc, cur) => (acc += cur), 0);
    if (sum > prev) {
      answer = i;
      prev = sum;
    }
  }

  return answer;
}
