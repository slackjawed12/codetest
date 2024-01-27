function areSimilar(mat: number[][], k: number): boolean {
  const shifted = mat.map((r) => r.slice());
  for (let i = 0; i < k; i++) {
    for (let row = 0; row < mat.length; row++) {
      if (row % 2 === 1) {
        const x = shifted[row].pop();
        shifted[row].unshift(x);
      } else {
        const x = shifted[row][0];
        shifted[row].shift();
        shifted[row].push(x);
      }
    }
  }

  for (let row = 0; row < mat.length; row++) {
    for (let col = 0; col < mat[row].length; col++) {
      if (mat[row][col] !== shifted[row][col]) {
        return false;
      }
    }
  }
  return true;
}
