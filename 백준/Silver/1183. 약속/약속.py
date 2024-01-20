import sys

N = int(sys.stdin.readline().strip())
times = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
diffs = [time[0] - time[1] for time in times]

diffs.sort()

if len(diffs) % 2 == 1:
    print(1)
else:
    print(diffs[len(diffs) // 2] - diffs[len(diffs) // 2 - 1] + 1)
