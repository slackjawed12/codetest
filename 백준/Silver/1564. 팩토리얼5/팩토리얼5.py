import sys

N = int(sys.stdin.readline().strip())

answer = 1
for i in range(1, N+1):
    answer *= i
    while answer % 10 == 0:
        answer //= 10

    answer %= 10000000000000

print("0"*(5-len(str(answer%100000)))+str(answer%100000))
