# 다리 놓기
import sys


class Solution:
    def solve(self, n: int, m: int) -> int:
        dp = [[0] * (m + 1) for i in range(n + 1)]
        dp[0] = [1] * (m + 1)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

            dp.append(dp[n - 1] + dp[n - 2])

        return dp[n][m]


def main():
    T = int(sys.stdin.readline().strip())
    answer = []
    for i in range(T):
        n, m = list(map(int, sys.stdin.readline().strip().split()))
        sol = Solution()
        a = sol.solve(n, m)
        answer.append(a)

    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
