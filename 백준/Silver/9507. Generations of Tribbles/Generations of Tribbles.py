import sys


def input_variables():
    test_case = int(sys.stdin.readline().strip())
    numbers = list(map(int, [sys.stdin.readline().strip() for _ in range(test_case)]))

    return [test_case, *numbers]


def fibo(num):
    dp = [0] * 69
    dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 4
    if num <= 3:
        return dp[num]

    for i in range(4, num+1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

    return dp[num]


T, *nums = input_variables()
answer = [str(fibo(n)) for n in nums]

print("\n".join(answer))
