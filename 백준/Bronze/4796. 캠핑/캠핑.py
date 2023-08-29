import sys

i = 1
arr = []
while True:
    L, P, V = list(map(int, sys.stdin.readline().split()))

    if L == 0 and P == 0 and V == 0:
        print("\n".join(arr))
        break

    r = V % P
    q = V // P
    res = L if L <= r else r
    arr.append(f"Case {i}: {q*L+res}")
    i += 1

