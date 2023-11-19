import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
numbers.sort()
result = 10_000_000_000
answer = 0
for n in range(numbers[-1], numbers[0]-1, -1):
    diff_sum = sum([abs(x-n) for x in numbers])
    if diff_sum <= result:
        result = diff_sum
        answer = n

print(answer)