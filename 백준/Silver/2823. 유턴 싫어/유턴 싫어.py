import sys
from collections import deque

R, C = list(map(int, sys.stdin.readline().strip().split()))
board = [list(sys.stdin.readline().strip()) for _ in range(R)]


def bfs(startX, startY):
    visit = [[False] * C for _ in range(R)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    q = deque([[startX, startY]])
    while len(q) > 0:
        count = 0
        cx, cy = q.pop()
        for i in range(4):
            nx = dx[i] + cx
            ny = dy[i] + cy
            if 0 <= nx < C and 0 <= ny < R and board[ny][nx] == '.':
                count += 1
                if not visit[ny][nx]:
                    visit[ny][nx] = True
                    q.append([nx, ny])

        if count <= 1:
            return 1

    return 0


sx, sy = -1, -1
for row in range(R):
    for col in range(C):
        if board[row][col] == '.':
            sx, sy = col, row
            break
    if sx != -1 and sy != -1:
        break

result = bfs(sx, sy)
print(result)
