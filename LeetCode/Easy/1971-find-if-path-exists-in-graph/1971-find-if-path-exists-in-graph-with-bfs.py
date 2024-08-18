from collections import deque

class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = self.init(n, edges)
        print(adj)

        visit = [False]*(n)
        q = deque([source])
        visit[source] = True
        while q:
            cur = q.pop()
            for nv in adj[cur]:
                if not visit[nv]:
                    visit[nv] = True
                    q.append(nv)
        
        return visit[destination]
    
    def init(self, n: int, edges: list[list[int]])->dict:
        result = {i:[] for i in range(n)}
        for s, e in edges:
            result[s].append(e)
            result[e].append(s)
        
        return result