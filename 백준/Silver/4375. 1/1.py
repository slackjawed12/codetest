import sys

inputs = list(map(int, sys.stdin.readlines()))

result = []
for n in inputs:
    start, count = 1, 1
    sum = start % n
    res = 1
    while sum % n != 0:
        start = start * 10
        temp = (res % n) * (start % n)
        temp = temp % n
        sum += temp
        count += 1

    result.append(count)

for r in result:
    print(r)
