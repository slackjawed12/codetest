import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
prices = [int(sys.stdin.readline().strip()) for _ in range(M)]
prices.sort()
answer = [0, 0]
for i, p in enumerate(prices):
    expected = p * (min(len(prices) - i, N))
    if expected > answer[1]:
        answer = [p, expected]

print(*answer)
