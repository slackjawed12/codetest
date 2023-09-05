import sys

W, H = list(map(int, sys.stdin.readline().strip().split()))
N = int(sys.stdin.readline().strip())

row, col = [0], [0]
for _ in range(N):
    direction, index = list(map(int, sys.stdin.readline().strip().split()))
    if direction == 0:
        row.append(index)
    else:
        col.append(index)

row.append(H)
col.append(W)

row.sort()
col.sort()

rowMax, colMax = 0, 0
for i in range(len(row) - 1):
    diff = row[i + 1] - row[i]
    rowMax = max(diff, rowMax)

for i in range(len(col) - 1):
    diff = col[i + 1] - col[i]
    colMax = max(diff, colMax)

print(rowMax * colMax)
