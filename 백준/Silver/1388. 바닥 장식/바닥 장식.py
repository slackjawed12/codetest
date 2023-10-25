import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
visit = [list([0] * len(board[0])) for _ in range(len(board))]

answer = 0
for i, row in enumerate(board):
    for j, cur in enumerate(row):
        if visit[i][j] != 0:
            continue

        visit[i][j] = 1
        if cur == '-':
            k = j + 1
            while k < len(row) and board[i][k] == '-':
                visit[i][k] = 1
                k += 1
        else:
            k = i + 1
            while k < len(board) and board[k][j] == '|':
                visit[k][j] = 1
                k += 1

        answer += 1

print(answer)
