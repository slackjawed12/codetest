import sys

R, C = list(map(int, sys.stdin.readline().strip().split()))
pixels = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]
T = int(sys.stdin.readline().strip())

result = []
for r in range(R-2):
    for c in range(C-2):
        cur_pixels = []
        for i in range(r, r+3):
            for j in range(c, c+3):
                cur_pixels.append(pixels[i][j])
        cur_pixels.sort()
        result.append(cur_pixels[4])

print(len([x for x in result if x >= T]))