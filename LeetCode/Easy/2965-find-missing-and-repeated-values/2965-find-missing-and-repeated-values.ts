// O(n)
function findMissingAndRepeatedValues(grid: number[][]): number[] {
  const visit = Array.from(Array(grid.length * grid.length + 1), (_) => 0);
  visit[0] = 1;
  for (const row of grid) {
    for (const num of row) {
      visit[num]++;
    }
  }

  return [visit.indexOf(2), visit.indexOf(0)];
}

// O(1) space
function gridSum(grid: number[][], valueMap: (val: number) => number): number {
  return grid.reduce(
    (acc, row) => acc + row.reduce((a, cell) => a + valueMap(cell), 0),
    0
  );
}

function findMissingAndRepeatedValuesV2(grid: number[][]): number[] {
  const sumOfGrid = gridSum(grid, (a: number) => a);
  const sumOfSquareOfGrid = gridSum(grid, (a) => a ** 2);

  const numCells = grid.length * grid.length;
  const expectedSum = (numCells * (numCells + 1)) / 2;
  const expectedSquareSum =
    (numCells * (numCells + 1) * (2 * numCells + 1)) / 6;

  const difference = expectedSum - sumOfGrid; // b - a
  const squareDifference = expectedSquareSum - sumOfSquareOfGrid; // b ^2 - a ^2

  const aPlusB = squareDifference / difference;
  const a = (aPlusB - difference) / 2;
  const b = aPlusB - a;

  return [a, b];
}
