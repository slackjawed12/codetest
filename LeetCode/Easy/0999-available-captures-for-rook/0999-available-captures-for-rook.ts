function numRookCaptures(board: string[][]): number {
    const leftCatch = (board:string[][], x:number, y:number):number => {
        for(let i =x-1; i>=0; i--){
            if(board[y][i]==='B') return 0;
            
            if(board[y][i]==='p') return 1;
        }
        return 0;
    }
    
    const rightCatch = (board:string[][], x:number, y:number):number =>{
        for(let i =x+1; i<board[y].length; i++){
            if(board[y][i]==='B') return 0;
            
            if(board[y][i]==='p') return 1;
        }
        return 0;
    }
    
    const upCatch = (board:string[][], x:number, y:number):number =>{
        for(let i =y-1; i>=0; i--){
            if(board[i][x]==='B') return 0;
            
            if(board[i][x]==='p') return 1;
        }
        return 0;
    }
    
    const downCatch = (board:string[][], x:number, y:number):number => {
        for(let i =y+1; i<board[y].length; i++){
            if(board[i][x]==='B') return 0;
            
            if(board[i][x]==='p') return 1;
        }
        return 0;
    }
    
    const findRook = (board:string[][]):[number,number] =>{
        const y = board.findIndex(row=>row.includes("R"));
        const x = board[y].findIndex(col=>col==='R');
        return [x, y];
    }
    const [x, y] = findRook(board);
    return leftCatch(board, x, y) + rightCatch(board, x, y) + upCatch(board, x, y) + downCatch(board, x, y);
};