import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))


def max_move(height, width):
    if height == 1:
        return 1
    elif height < 3:
        if width > 7:
            return 4
        elif width % 2 == 0:
            return width // 2
        else:
            return width // 2 + 1
    else:
        if width >= 7:
            return width - 2
        elif width == 6 or width == 5:
            return 4
        else:
            return width


print(max_move(N, M))
