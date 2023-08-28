import sys
N = int(input())
P = list(map(int, sys.stdin.readline().split()))

dp = [0]*N

for i in range(1, N):
    if P[i] > P[i-1]:
        dp[i]=dp[i-1]+P[i]-P[i-1]
    else:
        dp[i]=0

print(max(dp))