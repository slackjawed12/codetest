import sys

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(board, start):
    return dfs_helper(start, 0, "")


result = set([])


def dfs_helper(start, depth, cur):
    if depth == 6:
        result.add(cur)
        return

    for i in range(4):
        nx = start[0] + dx[i]
        ny = start[1] + dy[i]
        if 0 <= nx <= 4 and 0 <= ny <= 4:
            dfs_helper([nx, ny], depth + 1, cur + str(board[ny][nx]))


for y, row in enumerate(board):
    for x, num in enumerate(row):
        start = [x, y]
        dfs(board, start)

print(len(result))
