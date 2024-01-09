function kWeakestRows(mat: number[][], k: number): number[] {
  const indices = Array.from(Array(mat.length), (_, i) => i);
  indices.sort((r1, r2) => {
    const numOfOne1 = mat[r1].filter((v) => v === 1).length;
    const numOfOne2 = mat[r2].filter((v) => v === 1).length;
    if (numOfOne1 !== numOfOne2) {
      return numOfOne1 - numOfOne2;
    }

    return r1 - r2;
  });

  return indices.slice(0, k);
}
