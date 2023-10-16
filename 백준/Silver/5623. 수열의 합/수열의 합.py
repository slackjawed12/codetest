import sys

N = int(sys.stdin.readline().strip())
infos = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

answer =[]
if len(infos) == 2:
    answer = [1,1]
else:
    start = (-infos[1][2] + infos[0][1] + infos[0][2])//2
    answer = [infos[0][i]-start if i != 0 else start for i in range(N)]

print(*answer)

