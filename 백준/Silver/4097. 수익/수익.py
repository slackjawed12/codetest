import sys

answer = []
while True:
    N = int(sys.stdin.readline().strip())
    if N == 0:
        break

    numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]
    dp = [0] * (N + 1)
    dp[1] = numbers[0]
    for i in range(2, N + 1):
        dp[i] = max(dp[i - 1] + numbers[i - 1], numbers[i - 1])

    answer.append(max(dp[1:]))

for a in answer:
    print(a)
