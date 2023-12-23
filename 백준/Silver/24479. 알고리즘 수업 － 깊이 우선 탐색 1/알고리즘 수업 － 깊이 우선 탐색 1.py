import sys
sys.setrecursionlimit(10**6)
N, M, R = list(map(int, sys.stdin.readline().strip().split()))
connection_inputs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]


def init_graph():
    graph = {num: [] for num in range(1,N+1)}
    for connection in connection_inputs:
        graph[connection[0]].append(connection[1])
        graph[connection[1]].append(connection[0])

    for v in graph:
        graph[v].sort()

    return graph


visit = [0] * (N+1)
count = 0
def dfs(graph, start):
    global count
    if visit[start] == 0:
        visit[start] = count+1
        count += 1

        for next_vertex in graph[start]:
            if visit[next_vertex] == 0:
                dfs(graph, next_vertex)


graph = init_graph()
dfs(graph, R)
for i in visit[1:]:
    print(i)
