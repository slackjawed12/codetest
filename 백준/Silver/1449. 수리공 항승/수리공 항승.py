N, L, *position = list(map(int, open(0).read().split()))

position = sorted(position)

cur = 0
answer = 0
for i in range(N - 1):
    diff = position[i + 1] - position[i]
    if cur + diff >= L:
        answer += 1
        cur = 0
    else:
        cur += diff

answer += 1
print(answer)