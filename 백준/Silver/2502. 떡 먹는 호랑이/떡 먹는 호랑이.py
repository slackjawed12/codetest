# x, y
# x, y, x+y, x+2y 2x+3y, 3x+5y, 5x+8y
# 3x+5y=41
import sys


class Solution:
    def __init__(self):
        self.day, self.cake = list(map(int, sys.stdin.readline().strip().split()))

    def get_first_second_cake(self):
        a, b = self.get_multiple()
        first, second = 1, 0
        last_cake = self.cake
        while (last_cake - a * first) % b != 0:
            first += 1

        second = (last_cake - a * first) // b
        return [first, second]

    def get_multiple(self):
        dp = [0] * self.day
        dp[1] = 1
        dp[2] = 1
        for i in range(3, self.day):
            dp[i] = dp[i - 1] + dp[i - 2]

        return [dp[self.day - 2], dp[self.day - 1]]


sol = Solution()
answer = sol.get_first_second_cake()
print(answer[0])
print(answer[1])
