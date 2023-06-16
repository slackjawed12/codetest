N, M = map(int, input().split())
rect = [input() for _ in range(N)]

answer = 0
for r, row in enumerate(rect):
    for c, num in enumerate(list(row)):
        x, y, temp = c, r, 0
        while x < M and y < N:
            if num == rect[y][x] and num == rect[r][x] and num == rect[y][c]:
                temp = y - r + 1
            x += 1
            y += 1

        if temp * temp > answer:
            answer = temp * temp

print(answer)