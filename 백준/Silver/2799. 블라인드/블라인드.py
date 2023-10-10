import sys

M, N = list(map(int, sys.stdin.readline().strip().split()))
picture = [sys.stdin.readline().strip() for _ in range(5 * M + 1)]
start_points = []
for i in range(M):
    for j in range(N):
        start_points.append((i * 5 + 1, j * 5 + 1))

result = [0] * 5
for point in start_points:
    count = 0
    for k in range(4):
        if picture[point[0] + k][point[1]] == '*':
            count += 1

    result[count] += 1

print(*result)
