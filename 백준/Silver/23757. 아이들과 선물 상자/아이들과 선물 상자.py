import sys
import heapq

N, M = list(map(int, sys.stdin.readline().strip().split()))
gifts = [-x for x in list(map(int, sys.stdin.readline().strip().split()))]
children = list(map(int, sys.stdin.readline().strip().split()))

answer = 1
heapq.heapify(gifts)
for want in children:
    counts = heapq.heappop(gifts)
    if want > abs(counts):
        answer = 0
        break
    else:
        heapq.heappush(gifts, counts + want)

print(answer)
