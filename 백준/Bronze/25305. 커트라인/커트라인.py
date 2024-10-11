# 커트라인
import sys
from typing import List


class Solution:
    def solve(self, k: int, scores: List[int]) -> int:
        scores.sort()

        return scores[-k]


def main():
    N, k = list(map(int, (sys.stdin.readline().strip().split())))
    arr = list(map(int, sys.stdin.readline().strip().split()))
    sol = Solution()
    answer = sol.solve(k, arr)
    print(answer)


if __name__ == '__main__':
    main()
