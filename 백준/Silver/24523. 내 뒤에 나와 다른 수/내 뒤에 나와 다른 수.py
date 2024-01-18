import sys
from collections import deque
N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
conti = 1
lasts = {}
for index, num in enumerate(numbers):
    if index < len(numbers) - 1 and num != numbers[index + 1]:
        if num not in lasts:
            lasts[num] = deque([])

        while conti != 0:
            lasts[num].append(index + 2)
            conti -= 1

        conti = 1
    else:
        conti += 1

if numbers[-1] not in lasts:
    lasts[numbers[-1]] = deque([])

while conti != 0:
    lasts[numbers[-1]].append(-1)
    conti -= 1

result = [lasts[num].popleft() for num in numbers]
print(*result)
