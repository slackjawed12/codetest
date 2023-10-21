function numSpecial(mat: number[][]): number {
    let answer = 0;
    
    for(let i=0; i<mat.length; i++) {
        for (let j=0; j<mat[0].length; j++){
            if(mat[i][j]===0)
                continue;
            
            let isAllZero = true;
            for(let r=0; r < mat.length; r++) {
                if (r !== i) {
                    isAllZero &&= mat[r][j] === 0   
                }
            }
            
            for(let c=0; c < mat[0].length; c++) {
                if (c !== j) {
                    isAllZero &&= mat[i][c] === 0
                }
            }
            
            answer += isAllZero ? 1 : 0;
        }
    }
    
    return answer;
};