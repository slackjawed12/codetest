import sys

A, B, N = list(map(int, sys.stdin.readline().split()))

A = A % B
i = 0
result = 0
while i != N:
    A *= 10
    Q = A // B
    A -= B * Q
    result = Q
    i += 1

print(result)