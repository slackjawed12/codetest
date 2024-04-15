class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            row_nums = [c for c in row if c != '.']
            if len(set(row_nums)) != len(row_nums):
                return False
            
        for x in range(9): 
            col_nums = [board[y][x] for y, row in enumerate(board) if board[y][x] != '.']
            if len(set(col_nums)) != len(col_nums):
                return False
        
        for y in range(0,9,3):
            for x in range(0,9,3):
                sub = []
                for i in range(3):
                    for j in range(3):
                        sub.append(board[y+i][x+j])
                sub_nums = [num for num in sub if num != '.']

                if len(set(sub_nums)) != len(sub_nums):
                    return False

        return True
        