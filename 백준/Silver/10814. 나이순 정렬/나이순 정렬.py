# 나이순 정렬
import sys
from typing import List, Tuple


class Solution:
    def solve(self, pair: List[Tuple[str, ...]]) -> List[tuple[int, str]]:
        temp = [(i, int(p[0]), p[1]) for i, p in enumerate(pair)]
        temp.sort(key=lambda x: (x[1], x[0]))
        return [(p[1], p[2]) for p in temp]


def main():
    N = int(sys.stdin.readline().strip())
    tuples = [tuple(sys.stdin.readline().strip().split()) for _ in range(N)]
    sol = Solution()
    answer = sol.solve(tuples)

    for a in answer:
        print(*a)


if __name__ == '__main__':
    main()
