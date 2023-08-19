T = int(input())

answer = []
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    req = sum(arr)
    day = 1
    while N >= req:
        day += 1
        req *= 4
    answer.append(day)

for i in answer:
    print(i)

