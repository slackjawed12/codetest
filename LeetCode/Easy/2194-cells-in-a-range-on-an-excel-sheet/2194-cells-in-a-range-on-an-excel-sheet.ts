function cellsInRange(s: string): string[] {
  const [start, end] = s.split(":");
  const [startCol, startRow] = start.split("");
  const [endCol, endRow] = end.split("");
  let [curCol, curRow] = [startCol, startRow];
  let answer: string[] = [];
  while (curCol !== endCol || curRow !== endRow) {
    answer.push(curCol + curRow);
    if (curRow === endRow) {
      curRow = startRow;
      curCol = String.fromCharCode(curCol.charCodeAt(0) + 1);
    } else {
      curRow = String.fromCharCode(curRow.charCodeAt(0) + 1);
    }
  }
  answer.push(curCol + curRow);
  return answer;
}
