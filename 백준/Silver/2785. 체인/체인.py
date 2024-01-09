import sys
from collections import deque

N = int(sys.stdin.readline().strip())
chains = (list(map(int, sys.stdin.readline().strip().split())))

chains.sort()
q = deque(chains)
answer = 0
while len(q) > 1:
    split_chain = q.popleft()
    target_first = q.pop()

    if len(q) == 0:
        q.append(target_first + split_chain)
        answer += 1
    else:
        target_second = q.pop()
        q.append(target_first + target_second + 1)
        if split_chain > 1:
            q.appendleft(split_chain - 1)
        answer += 1

print(answer)
