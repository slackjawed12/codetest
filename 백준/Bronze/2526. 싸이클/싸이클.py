import sys

N, P = list(map(int, sys.stdin.readline().strip().split()))

S = {N: 0}

nextNum = N * N % P
index = 1
while nextNum not in S:
    S[nextNum] = index
    nextNum = (nextNum * N) % P
    index += 1

print(index-S[nextNum])
