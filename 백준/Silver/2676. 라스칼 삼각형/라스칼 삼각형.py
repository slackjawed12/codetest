import sys

T = int(sys.stdin.readline().strip())
answer = []

for _ in range(T):
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    answer.append(1 + (n - m) * m)

for a in answer:
    print(a)
