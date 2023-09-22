import sys

result = []

while True:
    N, M = list(map(int, sys.stdin.readline().strip().split(" ")))
    if N == 0 and M == 0:
        break

    A, B = [], []
    for _ in range(N):
        A.append(int(sys.stdin.readline().strip()))

    for _ in range(M):
        B.append(int(sys.stdin.readline().strip()))

    i, j, common = 0, 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            common += 1
            i += 1
            j += 1
        elif A[i] > B[j]:
            j += 1
        else:
            i += 1

    result.append(str(common))

print("\n".join(result))
