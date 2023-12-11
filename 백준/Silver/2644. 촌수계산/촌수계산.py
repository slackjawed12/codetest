import sys

n = int(sys.stdin.readline().strip())
a, b = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
relations = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

graph = {x: [] for x in range(1, n + 1)}
for relation in relations:
    graph[relation[0]].append(relation[1])
    graph[relation[1]].append(relation[0])

ans = [-1]

def dfs(graph, start, depth, visit, result):
    if start == b:
        result[0] = depth

    for adj in graph[start]:
        if not visit[adj]:
            visit[adj] = True
            dfs(graph, adj, depth + 1, visit, result)


dfs(graph, a, 0, [False] * (n + 1), ans)
print(ans[0])
