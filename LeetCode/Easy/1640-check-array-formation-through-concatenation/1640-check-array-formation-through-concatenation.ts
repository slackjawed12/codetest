function canFormArray(arr: number[], pieces: number[][]): boolean {
  const heads = pieces.reduce((prev, cur, index) => {
    prev.set(cur[0], index);
    return prev;
  }, new Map());

  let result: number[] = [];
  for (const num of arr) {
    const index = heads.get(num);
    if (index === undefined) {
      continue;
    }

    const targetPiece = pieces[index];
    result = [...result, ...targetPiece];
  }

  return result.join("") === arr.join("");
}
