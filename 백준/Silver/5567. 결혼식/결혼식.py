# 결혼식
import sys
from typing import List
from collections import deque


class Solution:
    def solve(self, count: int, relations: List[List[int]]) -> int:
        adj = {(i + 1): [] for i in range(count)}
        for a, b in relations:
            adj[a].append(b)
            adj[b].append(a)

        visit = [-1] * (count + 1)
        q = deque([1])
        visit[1] = 0
        while q:
            cur = q.popleft()
            for nxt in adj[cur]:
                if visit[nxt] == -1:
                    visit[nxt] = visit[cur] + 1
                    q.append(nxt)
                    
        return len([v for v in visit if v == 1 or v == 2])


def main():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

    sol = Solution()
    answer = sol.solve(n, arr)

    print(answer)


if __name__ == '__main__':
    main()
