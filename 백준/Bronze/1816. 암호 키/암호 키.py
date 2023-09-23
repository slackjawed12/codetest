import sys

N = int(sys.stdin.readline().strip())
targets = []
for _ in range(N):
    targets.append(int(sys.stdin.readline().strip()))

result = []
for index, target in enumerate(targets):
    cur = 2
    while cur <= 1000000:
        if target % cur == 0:
            result.append("NO")
            break

        cur += 1

    if len(result) < index+1:
        result.append("YES")


print("\n".join(result))
