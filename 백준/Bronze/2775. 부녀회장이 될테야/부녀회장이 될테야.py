# 부녀회장이 될테야
import sys


class Solution:
    def solve(self, floor: int, num: int) -> int:
        dp = [[i for i in range(num + 1)]]
        for f in range(floor):
            temp = [0] * (num + 1)
            for i in range(1, num + 1):
                temp[i] = temp[i - 1] + dp[f][i]

            dp.append(temp)

        return dp[floor][num]


def main():
    T = int(sys.stdin.readline().strip())
    answer = []
    for i in range(T):
        k = int(sys.stdin.readline().strip())
        n = int(sys.stdin.readline().strip())
        sol = Solution()
        answer.append(sol.solve(k, n))

    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
