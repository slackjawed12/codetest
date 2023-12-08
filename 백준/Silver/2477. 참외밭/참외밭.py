import sys

N = int(sys.stdin.readline().strip())
lines = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(6)]


def area_of(lines):
    widths = [x[1] for x in lines if x[0] == 1 or x[0] == 2]
    heights = [x[1] for x in lines if x[0] == 3 or x[0] == 4]
    total_area = max(widths) * max(heights)
    clockwise = []
    for i in range(6):
        if is_line_clockwise(lines[i], lines[(i + 1) % 6]):
            clockwise.append([lines[i], lines[(i + 1) % 6]])

    sub_area = clockwise[0][0][1] * clockwise[0][1][1]
    return total_area - sub_area


def is_line_clockwise(a, b):
    if a[0] == 1:
        return b[0] == 3
    elif a[0] == 2:
        return b[0] == 4
    elif a[0] == 3:
        return b[0] == 2
    return a[0] == 4 and b[0] == 1


print(N * area_of(lines))
