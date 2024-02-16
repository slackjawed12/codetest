# 양
import sys
from collections import deque


class Solution:
    def __init__(self):
        self.row, self.col = list(map(int, sys.stdin.readline().strip().split()))
        self.board = [list(sys.stdin.readline().strip()) for _ in range(self.row)]

    def get_sheep_and_wolf(self):
        visit = [[False] * self.col for _ in range(self.row)]

        tot_sheep, tot_wolf = 0, 0
        for y in range(self.row):
            for x in range(self.col):
                if not visit[y][x] and (self.board[y][x] == '.' or self.board[y][x] == 'o' or self.board[y][x] == 'v'):
                    s, w = self.bfs(visit, x, y)
                    if s <= w:
                        tot_wolf += w
                    else:
                        tot_sheep += s

        return [tot_sheep, tot_wolf]

    def bfs(self, visit, start_x, start_y):
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        q = deque([(start_x, start_y)])
        visit[start_y][start_x] = True
        s, w = 0, 0
        while len(q) > 0:
            x, y = q.popleft()
            if self.board[y][x] == 'v':
                w += 1
            elif self.board[y][x] == 'o':
                s += 1

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < self.col and 0 <= ny < self.row and not visit[ny][nx]:
                    visit[ny][nx] = True
                    if self.board[ny][nx] == 'v' or self.board[ny][nx] == 'o' or self.board[ny][nx] == '.':
                        q.append((nx, ny))

        return [s, w]


sol = Solution()
answer = sol.get_sheep_and_wolf()
print(*answer)
