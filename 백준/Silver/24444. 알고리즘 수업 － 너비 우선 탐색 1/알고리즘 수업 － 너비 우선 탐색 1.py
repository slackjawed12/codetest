import sys
from collections import deque


def init_graph(inputs, counts):
    adj = {num: [] for num in range(1, counts + 1)}
    for info in inputs:
        adj[info[0]].append(info[1])
        adj[info[1]].append(info[0])

    for v in adj:
        adj[v].sort()

    return adj


def bfs(adj_list, start):
    visit = [0] * (len(adj_list) + 1)
    q = deque([start])
    visit[start] = 1
    count = 1
    while len(q) != 0:
        next_v = q.popleft()
        for vertex in adj_list[next_v]:
            if visit[vertex] == 0:
                visit[vertex] = count + 1
                q.append(vertex)
                count += 1

    return visit[1:]


N, M, R = list(map(int, sys.stdin.readline().strip().split()))
inputs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
adj = init_graph(inputs, N)
answer = bfs(adj, R)
for a in answer:
    print(a)
