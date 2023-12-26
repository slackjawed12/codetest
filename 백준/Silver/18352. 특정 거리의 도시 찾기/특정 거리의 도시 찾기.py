# 특정 거리의 도시 찾기
import sys
from collections import deque

N, M, K, X = list(map(int, sys.stdin.readline().strip().split()))
inputs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]


def init_graph(connection_input, num):
    adj = {x: [] for x in range(1, num + 1)}
    for connection in connection_input:
        adj[connection[0]].append(connection[1])

    return adj


def find_distance_with_bfs(adj, dist, start):
    visit = [-1] * (len(adj) + 1)
    visit[start] = 0
    q = deque([start])
    answer = []
    while len(q) != 0:
        cur_city = q.popleft()
        for next_city in adj[cur_city]:
            if visit[next_city] == -1:
                visit[next_city] = visit[cur_city] + 1
                q.append(next_city)
                if visit[cur_city] + 1 == dist:
                    answer.append(next_city)


    return answer


adj_list = init_graph(inputs, N)
answer = find_distance_with_bfs(adj_list, K, X)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
