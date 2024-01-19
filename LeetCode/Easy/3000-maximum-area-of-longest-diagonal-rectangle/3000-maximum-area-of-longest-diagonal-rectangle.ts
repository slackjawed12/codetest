function areaOfMaxDiagonal(dimensions: number[][]): number {
  const diagonals = dimensions.map((val) => {
    return {
      diag: Math.sqrt(val[0] * val[0] + val[1] * val[1]),
      area: val[0] * val[1],
    };
  });
  const maxLength = diagonals.reduce((acc, cur) => Math.max(acc, cur.diag), 0);
  const maxDiagonals = diagonals.filter((val) => val.diag === maxLength);
  const maxArea = maxDiagonals.reduce((acc, cur) => Math.max(acc, cur.area), 0);
  return maxArea;
}
