# 순열 사이클
import sys
from typing import List
from collections import deque


class Solution:
    def solve(self, nums: List[int]) -> int:
        adj = {(i + 1): n for i, n in enumerate(nums)}

        visit = [0] * (len(nums) + 1)
        cnt = 1
        for i in range(1, len(nums) + 1):
            if visit[i] != 0:
                continue

            q = deque([i])
            visit[i] = cnt
            while q:
                cur = q.popleft()
                np = adj[cur]
                if not visit[np]:
                    visit[np] = cnt
                    q.append(np)

            cnt += 1

        return cnt - 1


def main():
    T = int(sys.stdin.readline().strip())
    answer = []
    for i in range(T):
        n = int(sys.stdin.readline().strip())
        arr = list(map(int, sys.stdin.readline().strip().split()))
        sol = Solution()
        answer.append(sol.solve(arr))

    for a in answer:
        print(a)


if __name__ == '__main__':
    main()
