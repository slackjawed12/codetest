# 피보나치 수 2
import sys


class Solution:
    def solve(self, n: int) -> int:
        dp = [0,1]
        for n in range(2, n+1):
            dp.append(dp[n-1] + dp[n-2])

        return dp[n]


def main():
    n = int(sys.stdin.readline().strip())
    sol = Solution()
    answer = sol.solve(n)
    print(answer)


if __name__ == '__main__':
    main()
