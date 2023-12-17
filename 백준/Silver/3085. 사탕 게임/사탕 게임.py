# 사탕 게임
import sys

N = int(sys.stdin.readline().strip())
board = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]


def get_max_continuous_substring(string_list):
    result, cur_char, temp = 0, string_list[0], 0
    for c in string_list:
        if c == cur_char:
            temp += 1
        else:
            result = max(result, temp)
            cur_char = c
            temp = 1

    result = max(result, temp)
    return result


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
for i, row in enumerate(board):
    for j, col in enumerate(row):
        string_row = board[i]
        string_col = [board[k][j] for k, _ in enumerate(board)]
        answer = max(answer, get_max_continuous_substring(string_row), get_max_continuous_substring(string_col))
        for n in range(4):
            nx = dx[n] + j
            ny = dy[n] + i
            if 0 <= nx < len(row) and 0 <= ny < len(board) and board[i][j] != board[ny][nx]:
                board[i][j], board[ny][nx] = board[ny][nx], board[i][j]
                string_one = board[i]
                string_two = [board[k][j] for k, _ in enumerate(board)]
                string_three = board[ny]
                string_four = [board[k][nx] for k, _ in enumerate(board)]
                answer = max(answer, get_max_continuous_substring(string_one), get_max_continuous_substring(string_two),
                             get_max_continuous_substring(string_three), get_max_continuous_substring(string_four))
                board[i][j], board[ny][nx] = board[ny][nx], board[i][j]

print(answer)
