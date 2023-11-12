import sys

R, C = list(map(int, sys.stdin.readline().strip().split()))
board = [sys.stdin.readline().strip() for _ in range(R)]
words = []
for row in board:
    chunk = row.split('#')
    words += [w for w in chunk if len(w) > 1]

for i in range(C):
    col_str = ""
    for j in range(R):
        col_str += board[j][i]

    chunk = col_str.split('#')
    words += [w for w in chunk if len(w) > 1]

words.sort()
print(words[0])