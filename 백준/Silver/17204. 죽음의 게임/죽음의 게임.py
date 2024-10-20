# 죽음의 게임
import sys
from typing import List
from collections import deque

class Solution:
    def solve(self, nums: List[int], k:int) -> int:
        visit = [-1]*(len(nums))
        q = deque([0])
        visit[0] = 0
        while q:
            cur = q.popleft()
            nx = nums[cur]
            if visit[nx] == -1:
                visit[nx] = visit[cur] + 1
                q.append(nx)

        return visit[k]


def main():
    n, k = list(map(int, sys.stdin.readline().strip().split()))
    arr = [int(sys.stdin.readline().strip()) for i in range(n)]
    sol = Solution()
    answer = sol.solve(arr, k)
    print(answer)


if __name__ == '__main__':
    main()
