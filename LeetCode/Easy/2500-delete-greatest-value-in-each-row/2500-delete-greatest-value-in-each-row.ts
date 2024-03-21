function deleteGreatestValue(grid: number[][]): number {
  const iterCount = grid[0].length;
  let answer = 0;
  for (let i = 0; i < iterCount; i++) {
    let maxDeleted = 0;
    for (let j = 0; j < grid.length; j++) {
      let index = 0;
      for (let k = 0; k < grid[j].length; k++) {
        if (grid[j][k] > grid[j][index]) {
          index = k;
        }
      }
      maxDeleted = Math.max(grid[j][index], maxDeleted);
      grid[j] = [...grid[j].slice(0, index), ...grid[j].slice(index + 1)];
    }
    answer += maxDeleted;
  }

  return answer;
}
