import sys

paper_size = 10
board = [[0] * 102 for _ in range(102)]
N = int(sys.stdin.readline().strip())
papers = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for paper in papers:
    start_y = paper[0]
    start_x = paper[1]
    for i in range(start_y, start_y + 10):
        for j in range(start_x, start_x + 10):
            board[i][j] = 1

result = 0
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]
for i in range(101):
    for j in range(101):
        if board[i][j] == 1:
            info = 0
            for k in range(4):
                if board[i + dy[k]][j + dx[k]] == 0:
                    info += 1
            if info == 2:
                result += 2
            elif info == 1:
                result += 1

print(result)
