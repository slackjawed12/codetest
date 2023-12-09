import sys
import math

N = int(sys.stdin.readline().strip())
dp = [0] * (N + 1)

i = 1
while i * i <= N:
    dp[i * i] = 1
    i += 1

for index in range(1, N + 1):
    if dp[index] != 0:
        continue

    j = 1
    while j * j <= index:
        comp = math.inf if dp[index] == 0 else dp[index]
        dp[index] = min(comp, dp[index - j * j] + dp[j * j])
        j += 1

print(dp[N])
