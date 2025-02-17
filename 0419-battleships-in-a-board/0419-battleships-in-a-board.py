class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visit = [[0]*len(row) for row in board]
        result = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and not visit[i][j]:
                    self.bfs(board, visit, (i, j))
                    result += 1

        return result

    def bfs(self, board, visit, start):
        q = deque([start])
        visit[start[0]][start[1]] = 1
        d = [(-1,0),(0,1),(1,0),(0,-1)]
        while q:
            cr, cc = q.popleft()
            for dr, dc in d:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    if board[nr][nc] == 'X' and not visit[nr][nc]:
                        q.append((nr, nc))
                        visit[nr][nc] = 1