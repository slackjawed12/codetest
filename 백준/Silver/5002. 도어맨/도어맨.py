import sys
from collections import deque

X = int(sys.stdin.readline().strip())
order = sys.stdin.readline().strip()

info = {'M': 0, 'W': 0}
q = deque(list(order))
while len(q) > 0 and abs(info['M'] - info['W']) <= X:
    if len(q) == 1:
        first = q.popleft()
        other = 'W' if first == 'M' else 'M'
        info[first] += 1 if info[first] - info[other] < X else 0
        continue

    more, less = ['M', 'W'] if info['M'] >= info['W'] else ['W', 'M']
    first = q.popleft()
    second = q.popleft()
    if first == less:
        info[first] += 1
        q.appendleft(second)
    elif second == less:
        info[second] += 1
        q.appendleft(first)
    else:
        if info[more] - info[less] < X:
            info[first] += 1
            q.appendleft(second)
        else:
            break

print(info['W'] + info['M'])
