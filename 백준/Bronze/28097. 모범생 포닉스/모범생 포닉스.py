import sys

a = input()
times = list(map(int, sys.stdin.readline().split()))
total = sum(times) + 8*(len(times)-1)
print(*[total // 24, total % 24])
