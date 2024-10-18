# 1로 만들기
import sys


class Solution:
    def solve(self, num: int) -> int:
        dp = [0] * (num + 1)
        for i in range(2, num + 1):
            if i % 2 == 0 and i % 3 == 0:
                dp[i] = min(dp[i - 1], dp[i // 2], dp[i // 3]) + 1
            elif i % 2 == 0:
                dp[i] = min(dp[i - 1], dp[i // 2]) + 1
            elif i % 3 == 0:
                dp[i] = min(dp[i - 1], dp[i // 3]) + 1
            else:
                dp[i] = dp[i - 1] + 1

        return dp[num]


def main():
    N = int(sys.stdin.readline().strip())
    sol = Solution()
    answer = sol.solve(N)
    print(answer)


if __name__ == '__main__':
    main()
