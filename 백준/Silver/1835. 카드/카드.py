from collections import deque
N = int(input())
desk = [i for i in range(1, N)]
q = deque([N])
while len(desk) != 0:
    q.appendleft(desk.pop())
    count = q[0]
    for i in range(count):
        q.appendleft(q.pop())

print(*q)