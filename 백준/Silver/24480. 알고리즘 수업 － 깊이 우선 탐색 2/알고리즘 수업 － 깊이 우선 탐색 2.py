import sys

sys.setrecursionlimit(10 ** 6)
N, M, R = list(map(int, sys.stdin.readline().strip().split()))
info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
graph = {i: [] for i in range(1, N + 1)}
for i in info:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for node in graph:
    graph[node].sort(reverse=True)


def dfs(graph, N):
    visit = [0] * (N + 1)
    dfs_helper(graph, visit, R, 0)
    return visit


def dfs_helper(graph, visit, cur, order):
    visit[cur] = order + 1
    result = order + 1
    for next_node in graph[cur]:
        if visit[next_node] == 0:
            result = dfs_helper(graph, visit, next_node, result)

    return result


result = dfs(graph, N)

for r in result[1:]:
    print(r)
