import sys

dp = []

for i in range(21):
    dp.append([[1] * 21 for j in range(21)])

for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                dp[i][j][k] = dp[i][j][k - 1] + dp[i][j - 1][k - 1] - dp[i][j - 1][k]
            else:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k] + dp[i - 1][j][k - 1] - dp[i - 1][j - 1][k - 1]

answer = []

while True:
    a, b, c = list(map(int, sys.stdin.readline().strip().split()))
    if a == -1 and b == -1 and c == -1:
        break
    else:
        value = 1 if (a <= 0 or b <= 0 or c <= 0) \
            else dp[20][20][20] if (a > 20 or b > 20 or c > 20) \
            else dp[a][b][c]
        answer.append(
            f'w({a}, {b}, {c}) = {value}')

for a in answer:
    print(a)
