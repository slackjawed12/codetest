class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(graph)
        visit = [False]*n
        def dfs(graph, cur, path):
            if cur == n-1:
                result.append(path[:])
                return
            
            for nx in graph[cur]:
                visit[nx] = True
                path.append(nx)
                dfs(graph, nx, path)
                path.pop()
        
        visit[0] = True
        dfs(graph, 0, [0])
        return result