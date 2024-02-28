# 보석 상자
import sys


class Solution:
    def __init__(self):
        self.n, self.m = list(map(int, sys.stdin.readline().strip().split()))
        self.candies = [int(sys.stdin.readline().strip()) for _ in range(self.m)]

    def solve(self):
        low, high = 1, max(self.candies)
        candy_per_kid = 1
        while low <= high:
            candy_per_kid = (low + high) // 2
            tot = 0
            for candy in self.candies:
                tot += (candy // candy_per_kid) if candy % candy_per_kid == 0 else (candy // candy_per_kid + 1)

            if tot > self.n:
                low = candy_per_kid + 1
            else:
                high = candy_per_kid - 1

        return low


sol = Solution()
print(sol.solve())
