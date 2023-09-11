N = int(input())

A, B, C = 1, 1, N - 2

count = 0
for A in range(1, N + 1):
    for B in range(A, N + 1):
        C = N - A - B

        if B > C:
            break

        if A + B > C >= B:
            count += 1

print(count)
