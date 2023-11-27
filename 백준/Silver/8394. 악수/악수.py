import sys

N = int(sys.stdin.readline().strip())
unit = [[0, 1], [1, 1]]
mat = [[0, 1], [1, 1]]


def mat_mul(A, B):
    temp = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] % 10) * (B[k][j] % 10)
                temp[i][j] %= 10

    return temp


while N > 0:
    if N % 2 == 0:
        unit = mat_mul(unit, unit)
        N //= 2
    else:
        mat = mat_mul(mat, unit)
        N -= 1

print(mat[1][0])
