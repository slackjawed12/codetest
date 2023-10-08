function diagonalSum(mat: number[][]): number {
    return mat.reduce((prev, row, index)=>{
        prev += row[index] + (row.length-1-index === index ? 0 :row[row.length-1-index]);
        return prev;
    },0)
};