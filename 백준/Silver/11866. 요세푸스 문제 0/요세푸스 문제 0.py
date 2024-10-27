# 요세푸스 문제 0
import sys
from typing import List
from collections import deque


class Solution:
    def solve(self, n: int, k: int) -> List[int]:
        q = deque(range(1, n + 1))
        result = []
        cnt = 1
        while q:
            if cnt % k == 0:
                result.append(q.popleft())
            else:
                q.append(q.popleft())

            cnt += 1

        return result


def main():
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    sol = Solution()
    answer = sol.solve(n, k)
    print("<" + ", ".join(list(map(str, answer))) + ">")


if __name__ == '__main__':
    main()
