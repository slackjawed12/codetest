import sys
from collections import deque


class Solution:
    def __init__(self, in_order, out_order):
        self.in_order = in_order
        self.out_order = out_order

    def solve(self):
        in_queue = deque(self.in_order)
        out_queue = deque(self.out_order)
        over = set([])
        while len(out_queue) > 0 and len(in_queue) > 0:
            in_first = in_queue.popleft()
            if in_first in over:
                continue

            out_first = out_queue.popleft()
            if in_first != out_first:
                over.add(out_first)
                in_queue.appendleft(in_first)

        return len(over)


def main():
    n = int(sys.stdin.readline().strip())
    in_order = [sys.stdin.readline().strip() for _ in range(n)]
    out_order = [sys.stdin.readline().strip() for _ in range(n)]
    sol = Solution(in_order, out_order)
    answer = sol.solve()
    print(answer)


main()
