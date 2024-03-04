# 행운의 문자열
import sys
from collections import Counter


class Solution:
    def __init__(self, origin):
        self.origin = origin
        self.counter = Counter(origin)

    def solve(self):
        return self.solve_helper('', 0)

    def solve_helper(self, prev, cur):
        answer = 0
        if cur == len(self.origin):
            return 1

        for key in self.counter.keys():
            if prev == key or self.counter[key] == 0:
                continue

            self.counter[key] -= 1
            answer += self.solve_helper(key, cur + 1)
            self.counter[key] += 1

        return answer


def main():
    s = sys.stdin.readline().strip()
    sol = Solution(s)
    print(sol.solve())


main()
