import sys

E, M, S = list(map(int, sys.stdin.readline().strip().split()))

ceil = [15, 28, 19]
cur = [1, 1, 1]
result = 1
while cur[0] != E or cur[1] != M or cur[2] != S:
    cur = list(map(lambda x: x[1] % ceil[x[0]] + 1, enumerate(cur)))
    result += 1

print(result)