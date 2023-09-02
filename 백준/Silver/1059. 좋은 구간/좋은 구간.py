import sys

L = int(sys.stdin.readline().strip())
S = list(map(int, sys.stdin.readline().strip().split()))
n = int(sys.stdin.readline().strip())

S = sorted(S)

if n in S:
    print(0)
else:
    i = 0
    while i < len(S) and n > S[i]:
        i += 1

    init = 1 if i == 0 else S[i - 1] + 1
    fin = S[i] - 1

    starts = list(range(init, n + 1))
    ends = list(map(lambda x: list(range(max(n, x + 1), fin + 1)), starts))
    result = sum(list(map(lambda x: len(x), ends)))

    print(result)