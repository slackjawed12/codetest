import sys

N = int(sys.stdin.readline().strip())
numbers=list(map(int, sys.stdin.readline().strip().split()))

numbers.sort(reverse=True)
result = 0
prev= numbers[0]
for num in numbers[1:]:
    result += prev*num
    prev = prev+num

print(result)