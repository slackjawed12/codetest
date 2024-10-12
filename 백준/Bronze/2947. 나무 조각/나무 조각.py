# 나무 조각
import sys
from typing import List


class Solution:
    def solve(self, arr: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(arr)):
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    result.append(arr.copy())

        return result


def main():
    inputs = list(map(int, sys.stdin.readline().strip().split()))
    sol = Solution()
    answer = sol.solve(inputs)

    for a in answer:
        print(*a)


if __name__ == '__main__':
    main()
