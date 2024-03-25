from collections import deque
def solution(board):
    temp = [list(row) for row in board]
    visit = [[-1]*len(board[0]) for row in board]
    answer = 0
    start, end = (0,0),(0,0)
    for y, row in enumerate(board):
        for x, c in enumerate(row):
            if temp[y][x] == 'R':
                start = (x,y)
            if temp[y][x] == 'G':
                end = (x,y)
                
    q = deque([start])
    visit[start[1]][start[0]] = 0
    direction = [(0,-1),(0,1),(-1,0),(1,0)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x, y
            prev = visit[y][x]
            while 0 <= nx < len(temp[0]) and 0 <= ny < len(temp) and temp[ny][nx] != 'D':
                nx,ny = nx + direction[i][0], ny + direction[i][1]
                    
            stopped = (nx-direction[i][0], ny - direction[i][1])
            if visit[stopped[1]][stopped[0]] == -1:
                visit[stopped[1]][stopped[0]] = prev+1
                q.append((stopped[0], stopped[1]))
            else:
                visit[stopped[1]][stopped[0]] = min(prev + 1, visit[stopped[1]][stopped[0]])
                    
    return visit[end[1]][end[0]]