import sys

N, K = list(map(int, sys.stdin.readline().strip().split()))
inputs = [sys.stdin.readline().strip().split() for _ in range(K)]
info = [[int(i[0]), i[1]] for i in inputs]

wheel = ['?'] * N
cur = 0
answer = []
for i in info:
    cur = (cur + i[0]) % N
    if wheel[cur] == '?':
        if i[1] in wheel:
            answer = '!'
            break
        else:
            wheel[cur] = i[1]
    elif wheel[cur] != i[1]:
        answer = '!'
        break

if answer != '!':
    answer = list(reversed(wheel[0:cur + 1])) + list(reversed(wheel[cur + 1:]))
    print("".join(answer))
else:
    print(answer)
