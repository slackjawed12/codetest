import sys


def input_data():
    R, C = list(map(int, sys.stdin.readline().strip().split()))
    board_input = [list(sys.stdin.readline().strip()) for _ in range(R)]
    return [R, C, board_input]


def get_first_word(board: list[list]):
    words = []
    horizontal_split = ["".join(row).split('#') for row in board]
    for row in horizontal_split:
        filtered = [w for w in row if len(w) >= 2]
        words += filtered

    for i in range(len(board[0])):
        vertical = "".join([row[i] for row in board])
        vertical_words = [w for w in vertical.split("#") if len(w) >= 2]
        words += vertical_words

    words.sort()
    return words[0]


R, C, board = input_data()
answer = get_first_word(board)
print(answer)
