import sys
from collections import deque

N = int(sys.stdin.readline().strip())
move_info = list(map(int, sys.stdin.readline().strip().split()))
circle = deque(list(enumerate(move_info)))
answer = []
while circle:
    index, number = circle.popleft()
    answer.append(index + 1)
    if number > 0:
        circle.rotate(-(number - 1))
    else:
        circle.rotate(-number)

print(*answer)
