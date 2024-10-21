# 연결 요소의 개수
import sys
from typing import List, Dict
from collections import deque


class Solution:
    def solve(self, info: List[List[int]], n: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v in info:
            adj[u].append(v)
            adj[v].append(u)

        visit = [0] * (n + 1)
        result = 0
        for v in adj.keys():
            if visit[v]:
                continue

            result = self.bfs(v, result, visit, adj)

        return result

    def bfs(self, start: int, cnt: int, visit: List[int], adj: Dict[int, List[int]]):
        q = deque([start])
        visit[start] = cnt + 1
        while q:
            cur = q.popleft()
            for n in adj[cur]:
                if not visit[n]:
                    visit[n] = cnt + 1
                    q.append(n)

        return cnt + 1


def main():
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    arr = [list(map(int, sys.stdin.readline().strip().split())) for i in range(m)]
    sol = Solution()
    answer = sol.solve(arr, n)
    print(answer)


if __name__ == '__main__':
    main()
