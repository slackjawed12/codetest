function shiftGrid(grid: number[][], k: number): number[][] { 
    let copied = grid.slice();
    for(let count=0; count<k; count++) {
        const temp = copied.map(row=>row.slice());
        for (let i=0; i<grid.length;i++){
            for(let j=0; j<grid[0].length; j++) {
                if((i === grid.length-1) && (j === grid[0].length - 1)) {
                    console.log(temp[0][0])
                    temp[0][0] = copied[i][j]
                } else if (j === grid[0].length - 1) {
                    temp[i+1][0] = copied[i][j]
                } else {
                    temp[i][j+1] = copied[i][j]
                }
                
            }
        }
        copied = temp.slice();
    }
    
    return copied;
};