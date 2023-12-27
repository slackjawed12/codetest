import sys
from collections import deque


def init_graph(edge_info, count):
    adj = {x: [] for x in range(1, count + 1)}
    for edge in edge_info:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    for v in adj:
        adj[v].sort(reverse=True)

    return adj


def bfs(graph, start):
    visit = [0] * (len(graph) + 1)
    visit[start] = 1
    q = deque([start])
    order = 1
    while len(q) != 0:
        cur_vertex = q.popleft()
        for next_vertex in graph[cur_vertex]:
            if visit[next_vertex] == 0:
                q.append(next_vertex)
                visit[next_vertex] = order + 1
                order += 1

    return visit[1:]


N, M, R = list(map(int, sys.stdin.readline().strip().split()))
edges = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

graph = init_graph(edges, N)
answer = bfs(graph, R)

for a in answer:
    print(a)
