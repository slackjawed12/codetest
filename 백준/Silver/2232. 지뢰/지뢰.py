import sys

N = int(sys.stdin.readline().strip())
mines = [-1] + [int(sys.stdin.readline().strip()) for _ in range(N)]
peaks = []
for i in range(1, N + 1):
    if i == N and mines[i - 1] <= mines[i]:
        peaks.append(i)
        continue

    if mines[i - 1] <= mines[i] and mines[i] >= mines[i + 1]:
        peaks.append(i)

for p in peaks:
    print(p)
