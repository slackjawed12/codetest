import sys

N, M = list(map(int, sys.stdin.readline().split()))
arr = []
for _ in range(N):
    arr.append(list(sys.stdin.readline().strip()))

emptyRow, emptyCol = [], []
for i, row in enumerate(arr):
    if 'X' not in row:
        emptyRow.append(i)

for j, cur in enumerate(arr[0]):
    col = [arr[r][j] for r in range(N)]
    if 'X' not in col:
        emptyCol.append(j)

print(max(len(emptyRow), len(emptyCol)))