N = int(input())

dp = [0] * 36
dp[0] = 1
for i in range(1, 36):
    for j in range(i):
        dp[i] += dp[i - j-1] * dp[j]

print(dp[N])
