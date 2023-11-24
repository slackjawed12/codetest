import sys

N = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]

first = 0
for i in range(0, len(numbers)):
    first = first + numbers[i] if i % 2 == 0 else first - numbers[i]

first //= 2

result = [first]
for i in range(0, N - 1):
    result.append(numbers[i] - result[i])

for r in result:
    print(r)
