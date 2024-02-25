import math
import sys


class Solution:
    def __init__(self):
        self.testcase = int(sys.stdin.readline().strip())
        self.testcases = []
        self.answers = []
        for _ in range(self.testcase):
            l, n = list(map(int, sys.stdin.readline().strip().split()))
            positions = [int(sys.stdin.readline().strip()) for _ in range(n)]
            self.testcases.append({'length': l, 'count': n, 'positions': positions})

    def solve(self):
        for case in self.testcases:
            answer = self.get_min_max_time(case['length'], case['positions'])
            self.answers.append(answer)

        for answer in self.answers:
            print(*answer)

    @staticmethod
    def get_min_max_time(length: int, positions: list):
        min_time = -1
        max_time = -1
        for pos in positions:
            dist_to_start, dist_to_end = pos, length - pos
            far = max(dist_to_start, dist_to_end)
            near = min(dist_to_start, dist_to_end)
            min_time = max(min_time, near)
            max_time = max(max_time, far)

        return [min_time, max_time]


sol = Solution()
sol.solve()
