import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * (N + 1)
dp[1] = 1
for i in range(2, N + 1):
    cur_val = nums[i - 1]
    temp = 1
    for j in range(1, i):
        past_val = nums[j - 1]
        if cur_val < past_val:
            temp = max(dp[j] + 1, temp)

    dp[i] = temp

print(N - max(dp))
