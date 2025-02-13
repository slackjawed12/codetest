class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        board = self.init_board(grid)
        cnt = 0
        d = [(0,-1),(1,0),(0,1),(-1,0)]
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    q = deque([(i,j)])
                    board[i][j] = cnt + 1
                    mx = 0
                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in d:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                                q.append((nr,nc))
                                board[nr][nc] = cnt + 1
                            
                    cnt += 1
        
        return cnt
                
    def init_board(self, grid: List[str])-> List[List[int]]:
        n = len(grid)
        board= [[0]*(3*n) for i in range(3*n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    board[3*i+2][3*j] = -1
                    board[3*i+1][3*j+1] = -1
                    board[3*i][3*j+2] = -1
                elif grid[i][j] == '\\':
                    board[3*i][3*j] = -1
                    board[3*i+1][3*j+1] = -1
                    board[3*i+2][3*j+2] = -1

        return board