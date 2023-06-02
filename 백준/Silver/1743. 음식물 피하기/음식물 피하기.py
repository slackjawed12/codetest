import sys

def is_in_bound(x, y, xmax, ymax):
    return 0 <= x < xmax and 0 <= y < ymax

def search_bfs(x, y, corridor):
    queue = []
    queue.append((y, x))
    count = 0
    while(queue):
        cur = queue.pop()
        for d in direction:
            x = cur[1]+d[1]
            y = cur[0]+d[0]
            if is_in_bound(x, y, M, N) and corridor[y][x]==1 and not visited[y][x]:
                visited[y][x] = True
                queue.append((y, x))
                count+=1
    return count

N, M, K = list(map(int, sys.stdin.readline().split()))
corridor = [[0]*M for i in range(N)]

for i in range(K):
    y, x = list(map(int, sys.stdin.readline().split()))
    corridor[y-1][x-1] = 1

visited = [[False]*M for i in range(N)]
direction = [[-1, 0], [0,1], [1,0],[0,-1]]
answer =0

for r, row in enumerate(corridor):
    for c, value in enumerate(row):
        if value == 1 and not visited[r][c]:
            temp = search_bfs(c, r, corridor)
            answer = max(temp, answer)

print(answer)