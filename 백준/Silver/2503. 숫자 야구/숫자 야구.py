import sys

N = int(sys.stdin.readline())
rows = [sys.stdin.readline().strip() for _ in range(N)]
infos = [list(map(int, row.split(" "))) for row in rows]

arr = []
num = 123
while num <= 987:
    target = list(str(num))
    if '0' in target or len(set(target)) != 3:
        num += 1
        continue
    arr.append(target)
    num += 1

for info in infos:
    n, s, b = info
    query = list(str(n))
    temp = []

    for target in arr:
        strike, ball = 0, 0
        for index, digit in enumerate(query):
            if digit in target:
                if target.index(digit) == index:
                    strike += 1
                else:
                    ball += 1

        if strike == s and ball == b:
            temp.append(target)

    arr = temp

print(len(arr))
