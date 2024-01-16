import sys

inputs = [int(line.strip()) for line in sys.stdin.readlines()]
dp = [0] * 251
dp[1] = 1
dp[2] = 3
for num in range(3, 251):
    dp[num] = 2 * dp[num - 2] + dp[num - 1]

for i in inputs:
    if i == 0:
        print(1)
    else:
        print(dp[i])
