import sys

N, K = list(map(int, sys.stdin.readline().strip().split()))
bottles, answer = N, 0
while bin(bottles).count('1') > K:
    bottles += 1
    answer += 1

print(answer)
