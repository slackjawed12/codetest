N = int(input())
count = 0
for C in range(N // 3, N // 2 + 1):
    B = C
    A = N - (B + C)
    while B >= A:
        if A <= B <= C < A + B:
            count += 1
        B -= 1
        A += 1

print(count)