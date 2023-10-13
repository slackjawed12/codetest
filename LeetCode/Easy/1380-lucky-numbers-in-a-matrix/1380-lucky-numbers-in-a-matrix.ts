function luckyNumbers (matrix: number[][]): number[] {
    let result = [];
    for(let i=0; i<matrix.length; i++) {
        for(let j=0; j<matrix[0].length; j++) {
            const val = matrix[i][j];
            const row = matrix[i];
            const col = matrix.map(r=>r[j]);
            if(val === Math.min(...matrix[i]) && val === Math.max(...col)) {
                result.push(val)
            }
        }
    }
    
    return result;
};