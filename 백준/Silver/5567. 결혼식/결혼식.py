import sys
from collections import deque


def init_graph(info_input, num):
    adj = {n: [] for n in range(num + 1)}
    for info in info_input:
        adj[info[0]].append(info[1])
        adj[info[1]].append(info[0])

    return adj


def bfs(graph, num):
    q = deque([])
    visit = [0] * (num + 1)
    visit[1] = 1
    q.append(1)
    while len(q) != 0:
        cur_person = q.pop()
        if visit[cur_person] > 2:
            continue

        for next_person in graph[cur_person]:
            if visit[next_person] == 0:
                visit[next_person] = visit[cur_person] + 1
                q.append(next_person)
    return len([v for v in visit if v == 2 or v == 3])


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
inputs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

graph = init_graph(inputs, n)
result = bfs(graph, n)
print(result)
