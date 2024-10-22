# 촌수계산
import sys
from typing import List, Dict
from collections import deque


class Graph:
    def __init__(self, adj: Dict[int, List[int]]):
        self.adj = adj

    def dfs(self, cur: int, end: int) -> int:
        visit = [-1] * (len(self.adj.keys()) + 1)
        visit[cur] = 0
        self.helper(cur, end, visit)
        return visit[end]

    def helper(self, cur: int, end: int, visit: List[int]):
        if cur == end:
            return

        for n in self.adj[cur]:
            if visit[n] == -1:
                visit[n] = visit[cur] + 1
                self.helper(n, end, visit)

    def bfs(self, cur: int, end: int) -> int:
        visit = [-1] * (len(self.adj.keys()) + 1)
        q = deque([cur])
        visit[cur] = 0
        while q:
            cur = q.popleft()
            for n in self.adj[cur]:
                if visit[n] == -1:
                    visit[n] = visit[cur] + 1
                    q.append(n)

        return visit[end]


class Solution:
    def solve(self, total: int, start: int, end: int, info: List[List[int]]) -> int:
        adj = {i: [] for i in range(1, total + 1)}
        for x, y in info:
            adj[x].append(y)
            adj[y].append(x)

        graph = Graph(adj)
        result = graph.bfs(start, end)

        return result


def main():
    n = int(sys.stdin.readline().strip())
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    arr = [list(map(int, sys.stdin.readline().strip().split())) for i in range(m)]
    sol = Solution()
    answer = sol.solve(n, a, b, arr)
    print(answer)


if __name__ == '__main__':
    main()
