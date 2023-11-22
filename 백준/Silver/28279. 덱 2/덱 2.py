import sys
from collections import deque

N = int(sys.stdin.readline().strip())
commands = [sys.stdin.readline().strip() for _ in range(N)]

deq = deque()
for c in commands:
    if c[0] == '1':
        deq.appendleft(c.split()[1])
    elif c[0] == '2':
        deq.append(c.split()[1])
    elif c[0] == '3':
        print(deq.popleft() if len(deq) != 0 else -1)
    elif c[0] == '4':
        print(deq.pop() if len(deq) != 0 else -1)
    elif c[0] == '5':
        print(len(deq))
    elif c[0] == '6':
        print(1 if len(deq) == 0 else 0)
    elif c[0] == '7':
        print(deq[0] if len(deq) != 0 else -1)
    elif c[0] == '8':
        print(deq[-1] if len(deq) != 0 else -1)
