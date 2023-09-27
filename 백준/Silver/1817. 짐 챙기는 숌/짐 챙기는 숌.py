import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
weights = [] if N == 0 else list(map(int, sys.stdin.readline().strip().split()))

result = 0
cur = 0
for w in weights:
    if cur + w <= M:
        cur += w
    else:
        result += 1
        cur = w

if cur > 0:
    result += 1

print(result)
