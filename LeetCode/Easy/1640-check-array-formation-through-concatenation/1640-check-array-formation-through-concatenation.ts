function canFormArray(arr: number[], pieces: number[][]): boolean {
  const heads = pieces.reduce((prev, cur, index) => {
    prev.set(cur[0], index);
    return prev;
  }, new Map());

  // shift 연산 비효율
  while (arr.length !== 0) {
    if (heads.get(arr[0]) === undefined) {
      return false;
    }

    const targetPiece = pieces[heads.get(arr[0])];
    while (targetPiece.length !== 0 && arr[0] === targetPiece[0]) {
      arr.shift();
      targetPiece.shift();
    }
  }

  return true;
}

function canFormArrayV2(arr: number[], pieces: number[][]): boolean {
  const heads = pieces.reduce((prev, cur, index) => {
    prev.set(cur[0], index);
    return prev;
  }, new Map());

  let result: number[] = [];

  for (const num of arr) {
    const index = heads.get(num);
    // !index 로 적으면 0일때 true이므로 틀림
    if (index === undefined) {
      continue;
    }

    const targetPiece = pieces[index];
    result = [...result, ...targetPiece];
  }

  return result.join("") === arr.join("");
}
