import sys
from collections import deque


def input_data():
    m, n, k = list(map(int, sys.stdin.readline().strip().split()))
    rectangles = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(k)]
    return [m, n, k, rectangles]


def get_partition(rectangles, height, width):
    board = [[0] * width for _ in range(height)]
    visit = [[False] * width for _ in range(height)]

    for rectangle in rectangles:
        start_x, start_y, end_x, end_y = rectangle
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                board[y][x] = 1

    areas = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for y in range(height):
        for x in range(width):
            if board[y][x] == 1 or visit[y][x]:
                continue

            q = deque([(x, y)])
            visit[y][x] = True
            area = 0
            while len(q) > 0:
                x, y = q.popleft()
                area += 1
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < width and 0 <= ny < height and not visit[ny][nx]:
                        visit[ny][nx] = True
                        if board[ny][nx] == 0:
                            q.append((nx, ny))

            areas.append(area)

    areas.sort()
    return areas


def main():
    m, n, k, rectangles = input_data()
    areas = get_partition(rectangles, m, n)
    print(len(areas))
    print(*areas)


main()
