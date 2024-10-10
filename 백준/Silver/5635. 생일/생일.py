# 생일
import sys
from typing import List


class Solution:
    def solve(self, students: List[List[str]]) -> List[str]:
        result = [s[0] for s in sorted(students, key=lambda x: (int(x[3]), int(x[2]), int(x[1])))]
        return [result[-1], result[0]]


def main():
    N = int(sys.stdin.readline().strip())
    inputs = [sys.stdin.readline().strip().split() for _ in range(N)]
    sol = Solution()
    answer = sol.solve(inputs)

    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
