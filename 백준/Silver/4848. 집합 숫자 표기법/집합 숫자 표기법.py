import sys


def num_to_set(n):
    dp = [""] * (n + 1)
    dp[0] = "{}"
    for i in range(1, n + 1):
        dp[i] = "{"
        for j in range(i):
            dp[i] += dp[j]
            if j < i - 1:
                dp[i] += ","
        dp[i] += "}"

    return dp[n]


def set_to_num(s):
    i = len(s)
    while s[i - 1] == '}':
        i -= 1
    return len(s) - i - 1


T = int(sys.stdin.readline().strip())
answer = []
for _ in range(T):
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    answer.append(num_to_set(set_to_num(a) + set_to_num(b)))

for a in answer:
    print(a)
