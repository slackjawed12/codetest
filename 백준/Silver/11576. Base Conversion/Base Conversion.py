import sys

A, B = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
digits = list(map(int, sys.stdin.readline().strip().split()))

target = 0
unit = 1
digits.reverse()
for d in digits:
    target += d * unit
    unit *= A


answer = []
while target >= B:
    answer.append(target % B)
    target //= B

answer.append(target)
answer.reverse()

print(*answer)
