import sys

A, P = list(map(int, sys.stdin.readline().split()))

numSet = {}
result = [A]
num = A
while True:
    numSet[num] = 1
    digits = list(map(int, str(num)))
    squares = list(map(lambda x: x ** P, digits))
    num = sum(squares)
    if num in numSet:
        i = result.index(num)
        result = result[:i]
        break

    numSet[num] = 1
    result.append(num)

print(len(result))