class Solution {
    public boolean isInBound(int x, int y, int size){
        if(0<=x && x<size && 0<=y && y<size) return true;
        else return false;
    }
    
    public void check(int[][] board, int x, int y, int size) {
        for(int dy=-1; dy<=1; dy++){
            for(int dx=-1; dx<=1; dx++){
                if(isInBound(x+dx, y+dy, size) && board[y+dy][x+dx]==0) {
                        board[y+dy][x+dx]=-1;   
                }
            }
        }
    }
    
    public int solution(int[][] board) {
        int answer = 0;
        int n = board.length;
        for(int y=0; y<board.length; y++){
            for(int x=0; x<board[0].length; x++){
                if(board[y][x]==1) {
                    check(board, x, y, n);
                }        
            }
        }
        
        for(int i=0; i<board.length; i++){
            for(int j=0; j<board[0].length; j++){
                if(board[i][j]==0) answer++;
            }
        }
        return answer;
    }
}