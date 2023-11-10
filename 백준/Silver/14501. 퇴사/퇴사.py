import sys

N = int(sys.stdin.readline().strip())
data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [0] * (N + 2)
for i, info in enumerate(data):
    diff, income = info[0], info[1]
    cur_day, next_day = i + 1, i + 1 + diff

    dp[cur_day] = max(dp[cur_day - 1], dp[cur_day])
    if next_day <= len(dp) - 1:
        dp[next_day] = max(dp[next_day], dp[cur_day] + income)

dp[N + 1] = max(dp[N], dp[N + 1])
print(dp[N + 1])
