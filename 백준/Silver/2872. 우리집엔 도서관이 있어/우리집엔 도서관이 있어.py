import sys

N = int(sys.stdin.readline().strip())
books = [int(sys.stdin.readline().strip()) for _ in range(N)]

i = 0
while books[i] != N:
    i += 1

max_top = N
while i >= 0:
    if books[i] == max_top:
        max_top -= 1
    i -= 1

print(max_top)
