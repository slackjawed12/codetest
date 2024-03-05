# 그림
import sys
from collections import deque


class Solution:
    def __init__(self, row, col, board):
        self.row = row
        self.col = col
        self.board = board
        self.visit = [[False] * self.col for _ in range(self.row)]

    def solve(self):
        count, max_area = 0, 0
        for i in range(self.row):
            for j in range(self.col):
                if not self.visit[i][j] and self.board[i][j] == 1:
                    count += 1
                    max_area = max(self.bfs(j, i), max_area)

        return [count, max_area]

    def bfs(self, start_x, start_y):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        q = deque([(start_x, start_y)])
        area = 1
        self.visit[start_y][start_x] = True
        while len(q) > 0:
            cur_x, cur_y = q.popleft()

            for i in range(4):
                nx, ny = cur_x + dx[i], cur_y + dy[i]
                if 0 <= nx < self.col and 0 <= ny < self.row and not self.visit[ny][nx]:
                    self.visit[ny][nx] = True
                    if self.board[ny][nx] == 1:
                        q.append((nx, ny))
                        area += 1

        return area


def main():
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    sol = Solution(n, m, board)
    answer = sol.solve()
    print(answer[0])
    print(answer[1])

main()