function tictactoe(moves: number[][]): string {
    const board: string[][] = [['', '', ''],['', '', ''],['', '', '']];
    moves.forEach((move, index)=>{
        if(index%2)
            board[move[0]][move[1]] = 'O'
        else 
            board[move[0]][move[1]] = 'X'
    })
    
    const checkWinner = (board: string[][]): string => {
        for(let i=0; i<3; i++){
            if((board[i][0] !== '') && (board[i][0] === board[i][1]) && (board[i][1] === board[i][2]))
                return board[i][0];
        }
        
        for(let i=0; i<3; i++){
            if(board[0][i] !== '' && board[0][i] === board[1][i] && board[1][i] === board[2][i])
                return board[0][i];
        }
        
        if(board[0][0] !== '' && board[0][0] === board[1][1] && board[1][1] === board[2][2]) {
            return board[0][0];
        }
        
        if(board[0][2] !== '' && board[0][2] === board[1][1] && board[1][1] === board[2][0]) {
            return board[0][2];
        }

        return '';
    }
    
    const result = checkWinner(board);
    
    if(result === 'X')
        return 'A';
    
    if(result === 'O')
        return 'B';
    
    if(moves.length === 9)
        return "Draw";
    
    return "Pending";
};