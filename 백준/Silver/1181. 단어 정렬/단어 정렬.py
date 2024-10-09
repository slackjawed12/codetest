# 단어 정렬
import sys
from typing import List, Tuple


class Solution:
    def solve(self, words: List[str]) -> List[str]:
        return sorted(set(words), key=lambda x: (len(x), x))


def main():
    N = int(sys.stdin.readline().strip())
    inputs = [sys.stdin.readline().strip() for _ in range(N)]
    sol = Solution()
    answer = sol.solve(inputs)

    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
