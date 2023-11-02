import sys

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
x = int(sys.stdin.readline().strip())

numbers.sort()
i, j = 0, len(numbers) - 1
result = 0
while i < j:
    if numbers[i] + numbers[j] == x:
        result += 1
        i += 1
        j -= 1
    elif numbers[i] + numbers[j] < x:
        i += 1
    else:
        j -= 1

print(result)
