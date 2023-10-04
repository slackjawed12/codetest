import sys

a, b, c = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(3)]


def determine_triangle(A, B, C):
    size_ab = (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2
    size_bc = (B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2
    size_ca = (C[0] - A[0]) ** 2 + (C[1] - A[1]) ** 2
    length = [size_ab, size_bc, size_ca]
    length.sort()
    if length[2] ** 0.5 >= length[1] ** 0.5 + length[0] ** 0.5:
        return "X"
    elif length[2] == length[1] == length[0]:
        return "JungTriangle"
    elif length[1] == length[0] or length[1] == length[2]:
        if length[1] + length[0] < length[2]:
            return "Dunkak2Triangle"
        elif length[1] + length[0] == length[2]:
            return "Jikkak2Triangle"
        else:
            return "Yeahkak2Triangle"
    else:
        if length[1] + length[0] < length[2]:
            return "DunkakTriangle"
        elif length[1] + length[0] == length[2]:
            return "JikkakTriangle"
        else:
            return "YeahkakTriangle"


print(determine_triangle(a, b, c))
