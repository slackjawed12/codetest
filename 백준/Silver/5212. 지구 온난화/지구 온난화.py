# 지구 온난화
import sys

R, C = list(map(int, sys.stdin.readline().strip().split()))
map_array = [list(sys.stdin.readline().strip()) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
after_map = [['.'] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if map_array[r][c] == 'X':
            sea_count = 0
            for i in range(4):
                nx, ny = c + dx[i], r + dy[i]
                if 0 <= nx < C and 0 <= ny < R:
                    sea_count = sea_count + 1 if map_array[ny][nx] == '.' else sea_count
                else:
                    sea_count += 1
            if sea_count <= 2:
                after_map[r][c] = 'X'

min_x, min_y, max_x, max_y = 99, 99, 0, 0
for r in range(R):
    for c in range(C):
        if after_map[r][c] == 'X':
            min_x = min(c, min_x)
            min_y = min(r, min_y)
            max_x = max(c, max_x)
            max_y = max(r, max_y)

final_map = [row[min_x:max_x+1]for row in after_map[min_y:max_y+1]]

for row in final_map:
    print("".join(row))