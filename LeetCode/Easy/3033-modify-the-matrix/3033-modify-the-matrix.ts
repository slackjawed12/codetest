function modifiedMatrix(matrix: number[][]): number[][] {
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (matrix[i][j] !== -1) {
        continue;
      }

      for (let k = 0; k < matrix.length; k++) {
        matrix[i][j] = Math.max(matrix[i][j], matrix[k][j]);
      }
    }
  }

  return matrix;
}
