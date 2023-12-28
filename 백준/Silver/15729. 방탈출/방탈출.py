import sys

N = int(sys.stdin.readline().strip())
source = list(map(int, sys.stdin.readline().strip().split()))

answer = 0
cur = [0] * N
for i in range(N):
    if cur[i] == 0:
        if source[i] == 1:
            answer += 1
            cur[i] ^= 1
            if i < N - 1:
                cur[i + 1] ^= 1
            if i < N - 2:
                cur[i + 2] ^= 1
    else:
        if source[i] == 0:
            answer += 1
            cur[i] ^= 1
            if i < N - 1:
                cur[i + 1] ^= 1
            if i < N - 2:
                cur[i + 2] ^= 1


print(answer)