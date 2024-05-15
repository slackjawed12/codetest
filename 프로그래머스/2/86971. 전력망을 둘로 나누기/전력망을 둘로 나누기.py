from collections import deque
def solution(n, wires):
    graph = {}
    for wire in wires:
        start, end = wire
        if start in graph:
            graph[start].append([end, 0])
        else:
            graph[start] = [[end, 0]]
        if end in graph: 
            graph[end].append([start, 0])
        else:
            graph[end] = [[start, 0]]
            
    for vertex in graph.keys():
        visit = [False]*(n+1)
        visit[vertex] = True
        dfs(graph, vertex, visit)
    
    answer = n
    for edges in graph.values():
        for edge in edges:
            diff = abs(2*edge[1]- n)
            answer = min(diff, answer)
            
    return answer

def dfs(graph, vertex, visit):
    for edge in graph[vertex]:
        next_vertex, count = edge
        if not visit[next_vertex]:
            visit[next_vertex] = True
            edge[1] += dfs(graph, next_vertex, visit)
        
    return 1