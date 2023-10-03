import sys

board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(5)]
call = []
for _ in range(5):
    call += list(map(int, sys.stdin.readline().strip().split()))


def is_bingo(info):
    row = check_row_bingo(info)
    col = check_col_bingo(info)
    diag = check_diagonal_bingo(info)
    if row + col + diag >= 3:
        return True

    return False


def check_row_bingo(info):
    result = 0
    for r in info:
        if r.count(True) == len(r):
            result += 1

    return result


def check_col_bingo(info):
    result = 0
    for i in range(len(info[0])):
        temp = 0
        for j in range(len(info)):
            if info[j][i]:
                temp += 1

        if temp == len(info[0]):
            result += 1

    return result


def check_diagonal_bingo(info):
    result = 0
    dec = 0
    for i in range(len(info)):
        if info[i][i]:
            dec += 1

    if dec == len(info):
        result += 1

    inc = 0
    for j in range(len(info)):
        if info[j][len(info) - j - 1]:
            inc += 1

    if inc == len(info):
        result += 1

    return result


cur = [[False] * 5 for _ in range(5)]

answer = 0
for i, n in enumerate(call):
    for y, row in enumerate(board):
        for x, number in enumerate(row):
            if number == n:
                cur[y][x] = True

    if is_bingo(cur):
        answer = i + 1
        break

print(answer)
