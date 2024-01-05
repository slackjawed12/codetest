# 보이는 점의 개수
import sys


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def init_visible_counts():
    counts = [0] * 1001
    counts[1] = 3
    store = set("")
    for n in range(2, 1001):
        points = [[n, i] for i in range(1, n)]
        temp = 0
        for p in points:
            g = gcd(p[0], p[1])
            key = str(p[0] // g) + ":" + str(p[1] // g)
            if key not in store:
                store.add(key)
                temp += 1

        counts[n] = (temp * 2 + counts[n - 1])

    return counts


T = int(sys.stdin.readline().strip())
answer = []
counts = init_visible_counts()
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    answer.append(counts[N])

for a in answer:
    print(a)
