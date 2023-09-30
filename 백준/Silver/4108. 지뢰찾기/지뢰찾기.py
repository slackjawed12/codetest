import sys

answer = []
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
while True:
    R, C = list(map(int, sys.stdin.readline().strip().split()))
    if R == 0 and C == 0:
        break

    board = [list(sys.stdin.readline().strip()) for _ in range(R)]

    result = board
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            mine = 0
            if c == '.':
                for k in range(8):
                    x = j + dx[k]
                    y = i + dy[k]
                    if 0 <= x < len(row) and 0 <= y < len(board) and board[y][x] == '*':
                        mine += 1
                result[i][j] = str(mine)
            else:
                result[i][j] = '*'

    result = ["".join(r) for r in result]
    answer.append(result)

for a in answer:
    print("\n".join(a))
