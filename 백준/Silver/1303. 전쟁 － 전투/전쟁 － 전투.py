# 전쟁 - 전투
import sys
from collections import deque


class Solution:
    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        self.board = board

    def solve(self):
        white, black = 0, 0
        for i in range(self.row):
            for j in range(self.col):
                if self.board[i][j] == 'W':
                    white += self.bfs(j, i, self.board[i][j])
                elif self.board[i][j] == 'B':
                    black += self.bfs(j, i, self.board[i][j])

        return [white, black]

    def bfs(self, start_x, start_y, symbol):
        q = deque([(start_x, start_y)])
        score = 1
        self.board[start_y][start_x] = 'V'
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while len(q) > 0:
            cur_x, cur_y = q.popleft()
            for i in range(4):
                nx, ny = cur_x + dx[i], cur_y + dy[i]
                if 0 <= nx < self.col and 0 <= ny < self.row and self.board[ny][nx] == symbol:
                    q.append((nx, ny))
                    score += 1
                    self.board[ny][nx] = 'V'

        return score * score


def main():
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    board = [list(sys.stdin.readline().strip()) for _ in range(m)]
    sol = Solution(m, n, board)
    answer = sol.solve()
    print(*answer)


main()
