# 일곱 난쟁이
import sys
from typing import List


class Solution:
    def solve(self, heights: List[int]) -> List[int]:
        total = sum(heights)
        for i in range(len(heights) - 1):
            for j in range(i + 1, len(heights)):
                if total - heights[i] - heights[j] == 100:
                    return sorted(heights[:i] + heights[i + 1:j] + heights[j + 1:])

        return []


def main():
    arr = [int(sys.stdin.readline().strip()) for i in range(9)]
    sol = Solution()
    answer = sol.solve(arr)

    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
