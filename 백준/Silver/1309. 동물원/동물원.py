def input_data():
    n = int(input())
    return n


def get_combination(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 3
    for i in range(2, n + 1):
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901

    return dp[n]


def main():
    n = input_data()
    print(get_combination(n))


main()
