import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().strip().split()))
input_data = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]


def init_graph(data):
    graph = {}
    for pair in data:
        if pair[1] not in graph:
            graph[pair[1]] = [pair[0]]
        else:
            graph[pair[1]].append(pair[0])
    return graph


def bfs_hack(adj, visit, hack, start):
    visit[start] = True
    q = deque([start])
    cnt = 1
    while len(q) != 0:
        cur = q.popleft()
        if cur not in adj:
            hack[cur] = 1
            continue

        for node in adj[cur]:
            if not visit[node]:
                visit[node] = True
                cnt += 1
                q.append(node)

    hack[start] = cnt


adj = init_graph(input_data)
hack = [0] * (N + 1)
for start in adj:
    visit = [False] * (N + 1)
    bfs_hack(adj, visit, hack, start)

max_val = max(hack)
answer = [str(i) for i, v in enumerate(hack) if v == max_val]

print(" ".join(answer))