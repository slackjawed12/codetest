from heapq import heappush, heappop
import sys

N = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

heap = []
for row in reversed(board):
    for num in row:
        if len(heap) < N:
            heappush(heap, num)
        else:
            smallest = heap[0]
            if smallest < num:
                heappop(heap)
                heappush(heap, num)

print(heap[0])