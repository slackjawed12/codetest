class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for i in range(n)]
        for s,e in edges:
            g[e].append(s)

        return [i for i, arr in enumerate(g) if not arr]
        