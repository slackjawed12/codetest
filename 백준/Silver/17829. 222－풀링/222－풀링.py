def pool_helper(board, xi, yi, xf, yf) -> int:
    if xf - xi == 1:
        return sorted([board[yi][xi], board[yi][xf], board[yf][xi], board[yf][xf]])[2]

    x = pool_helper(board, xi, yi, (xi+xf) // 2, (yi+yf) // 2)
    y = pool_helper(board, (xi+xf) // 2 + 1, yi, xf, (yi+yf) // 2)
    z = pool_helper(board, xi, (yi+yf) // 2 + 1, (xi+xf) // 2, yf)
    w = pool_helper(board, (xi+xf) // 2 + 1, (yi+yf) // 2 + 1, xf, yf)
    return sorted([x, y, z, w])[2]


def pool(board) -> int:
    return pool_helper(board, 0, 0, len(board) - 1, len(board) - 1)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(pool(board))
