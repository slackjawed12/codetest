from collections import deque

def solution(maps):
    answer = []
    listed = [list(row) for row in maps]
    for i, row in enumerate(listed):
        for j, c in enumerate(row):
            if c != 'V' and c != 'X':
                answer.append(bfs(listed, j, i))
    
    if not answer:
        return [-1]
    
    answer.sort()
    return answer

def bfs(board, x, y):
    q = deque([(x,y)])
    d =[(-1,0),(0,-1),(1,0),(0,1)]
    result = int(board[y][x])
    board[y][x] = 'V'
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in d:
            nx, ny = cur_x + dx, cur_y + dy
            if 0 <= nx< len(board[0]) and 0 <= ny < len(board):
                if board[ny][nx] != 'V' and board[ny][nx] != 'X':
                    q.append((nx,ny))
                    result += int(board[ny][nx])
                    board[ny][nx] = 'V'
                    
    return result 
    