import sys

N = int(sys.stdin.readline().strip())
records = [sys.stdin.readline().strip() for _ in range(N)]

store = {}
answer = 0
for r in records:
    if r == 'ENTER':
        store ={}
    elif r not in store:
        store[r] = 1
        answer += 1

print(answer)