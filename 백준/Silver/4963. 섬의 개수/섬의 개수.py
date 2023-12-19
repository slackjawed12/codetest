import sys
from collections import deque


def get_count_island(sea_map):
    height, width = len(sea_map), len(sea_map[0])
    visit = [[False] * width for _ in range(height)]
    count = 0
    for r, row in enumerate(sea_map):
        for c, pos in enumerate(row):
            if not visit[r][c] and pos == 1:
                # bfs
                dx = [-1, 0, 1, -1, 1, -1, 0, 1]
                dy = [-1, -1, -1, 0, 0, 1, 1, 1]
                count += 1
                visit[r][c] = True
                q = deque([(c, r)])
                while len(q) != 0:
                    cur_x, cur_y = q.pop()
                    for i in range(8):
                        nx = dx[i] + cur_x
                        ny = dy[i] + cur_y
                        if 0 <= nx < width and 0 <= ny < height and not visit[ny][nx]:
                            visit[ny][nx] = True
                            if sea_map[ny][nx] == 1:
                                q.append((nx, ny))

    return count


answers = []
while True:
    w, h = list(map(int, sys.stdin.readline().strip().split()))
    if w == 0 and h == 0:
        break

    sea_map = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]

    answers.append(get_count_island(sea_map))

for answer in answers:
    print(answer)
