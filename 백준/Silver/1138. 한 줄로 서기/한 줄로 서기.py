import sys

N = int(input())
info = list(map(int, sys.stdin.readline().strip().split()))

result = [0] * N

for index, count in enumerate(info):
    position = 0
    zero = 0
    while zero < count or (zero == count and result[position] != 0):
        if result[position] == 0:
            zero += 1

        position += 1

    result[position] = index + 1

print(*result)
