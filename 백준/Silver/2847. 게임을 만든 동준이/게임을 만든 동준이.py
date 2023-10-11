import sys

N = int(sys.stdin.readline().strip())
scores = [int(sys.stdin.readline().strip()) for _ in range(N)]
scores.reverse()
answer = 0
for i, n in enumerate(scores[1:]):
    if scores[i+1] >= scores[i]:
        target = scores[i+1] - scores[i] + 1
        scores[i+1] -= target
        answer += target

print(answer)
