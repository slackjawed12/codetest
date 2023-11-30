import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
combinations = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

graph = {i: set([]) for i in range(1, N + 1)}
for combi in combinations:
    graph[combi[0]].add(combi[1])
    graph[combi[1]].add(combi[0])

answer = 0
for i in range(1, N + 1):
    second = [x for x in range(1, N + 1) if x > i and x not in graph[i]]
    for j in second:
        third = [y for y in range(1, N + 1) if y > j and y not in graph[j] and y not in graph[i]]
        for k in third:
            answer += 1

print(answer)
