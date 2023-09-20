import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))
J = int(sys.stdin.readline().strip())
pos = [int(sys.stdin.readline().strip()) for _ in range(J)]

bucket = range(1, M+1)
distance = 0
for cur in pos:
    if cur < bucket[0]:
        distance += bucket[0]-cur
        bucket = range(cur, cur+M)
    elif cur > bucket[len(bucket)-1]:
        distance += cur - bucket[len(bucket)-1]
        bucket = range(cur+1-M, cur+1)


print(distance)