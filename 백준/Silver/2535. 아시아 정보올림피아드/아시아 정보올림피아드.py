import sys

N = int(input())
info = []
for _ in range(N):
    info.append(list(map(int, sys.stdin.readline().strip().split())))

info.sort(key=lambda i: i[2], reverse=True)

gold, silver = [info[0][0], info[0][1]], [info[1][0], info[1][1]]

bronze = []
if gold[0] != silver[0]:
    bronze = [info[2][0], info[2][1]]
else:
    filtered = [x for x in info if x[0] != gold[0]]
    bronze = [filtered[0][0], filtered[0][1]]

print(*gold)
print(*silver)
print(*bronze)
